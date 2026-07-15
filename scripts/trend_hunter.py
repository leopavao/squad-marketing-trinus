#!/usr/bin/env python3
"""
Trend Hunter — Camada 1 (Inteligência) do squad.
Puxa sinal real via Apify: Instagram (concorrentes/referências) + Google Trends (keywords).
Escreve um radar em markdown que o editor-conteudo usa na Camada 2.

Uso:
    export APIFY_TOKEN=apify_api_xxx
    python3 trend_hunter.py marca/trend-config.json

Sem dependências externas (só stdlib). Limites pequenos de propósito: tier grátis Apify (US$5/mês).
"""
import json, os, sys, time, urllib.request, urllib.error, datetime

API = "https://api.apify.com/v2"

def _get(url, timeout=60):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode())

def call_actor(actor, payload, token, max_wait=900):
    """Dispara o run (async) e acompanha por polling — robusto pra actor lento."""
    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(f"{API}/acts/{actor}/runs?token={token}&memory=4096",
                                     data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            run = json.loads(r.read().decode())["data"]
        run_id, dsid = run["id"], run["defaultDatasetId"]
    except urllib.error.HTTPError as e:
        print(f"  [erro start {actor}] {e.code}: {e.read().decode()[:200]}", file=sys.stderr); return []
    except Exception as e:
        print(f"  [erro start {actor}] {e}", file=sys.stderr); return []

    waited = 0
    while waited < max_wait:
        time.sleep(8); waited += 8
        try:
            st = _get(f"{API}/actor-runs/{run_id}?token={token}")["data"]["status"]
        except Exception as e:
            print(f"  [erro poll {actor}] {e}", file=sys.stderr); return []
        if st == "SUCCEEDED":
            try:
                return _get(f"{API}/datasets/{dsid}/items?clean=true&token={token}", timeout=120)
            except Exception as e:
                print(f"  [erro dataset {actor}] {e}", file=sys.stderr); return []
        if st in ("FAILED", "ABORTED", "TIMED-OUT"):
            print(f"  [run {actor} terminou em {st}]", file=sys.stderr); return []
    print(f"  [timeout local {actor}: passou de {max_wait}s, run ainda rodando]", file=sys.stderr)
    return []

def instagram(profiles, posts_per, token):
    profiles = [h for h in profiles if h and "PREENCHER" not in h.upper()]
    if not profiles:
        print("  Instagram: nenhum @ real configurado (pulando). Preencha em trend-config.json.")
        return []
    urls = [{"url": f"https://www.instagram.com/{h.lstrip('@')}/"} for h in profiles]
    payload = {
        "directUrls": [u["url"] for u in urls],
        "resultsType": "posts",
        "resultsLimit": posts_per,         # poucos posts por perfil (tier grátis)
        "addParentData": False,
    }
    print(f"  Instagram: {len(profiles)} perfis x {posts_per} posts...")
    items = call_actor("apify~instagram-scraper", payload, token)
    out = []
    for it in items:
        out.append({
            "perfil": it.get("ownerUsername") or it.get("username"),
            "tipo": it.get("type"),
            "legenda": (it.get("caption") or "")[:240],
            "likes": it.get("likesCount"),
            "comentarios": it.get("commentsCount"),
            "url": it.get("url"),
            "data": it.get("timestamp"),
        })
    return out

def google_trends(keywords, geo, token):
    if not keywords: return []
    # actor leve, baseado em API (rápido, pouca memória) — substitui o oficial browser-based
    payload = {
        "keywords": keywords,
        "geo": geo,
        "hl": "pt-BR",
        "timeframe": "today 3-m",
        "include_related_queries": True,
        "include_related_topics": True,
    }
    print(f"  Google Trends: {len(keywords)} keywords (geo={geo}) via actor leve...")
    items = call_actor("s-r~free-google-trends-scraper", payload, token)
    return items

def write_radar(cfg, ig, gt, path):
    ig_sorted = sorted(ig, key=lambda p: (p.get("likes") or 0) + (p.get("comentarios") or 0), reverse=True)
    now = cfg.get("_stamp", "")
    lines = [f"# Radar de tendências — {cfg.get('cliente','')} ({now})", ""]
    lines += ["> Gerado pelo trend-hunter (Apify). Sinal bruto. O editor cruza com os pilares na Camada 2.", ""]
    lines += ["## O que os concorrentes/referências postaram (top por engajamento)", ""]
    if ig_sorted:
        for p in ig_sorted[:15]:
            eng = (p.get("likes") or 0) + (p.get("comentarios") or 0)
            lines.append(f"- **@{p['perfil']}** ({p.get('tipo')}, {eng} eng.): {p['legenda']}  \n  {p.get('url','')}")
    else:
        lines.append("_Sem dados de Instagram (checar token/handles na watchlist)._")
    lines += ["", "## Tendência de busca (Google Trends, últimos 3 meses)", ""]
    if gt:
        lines.append("```json")
        lines.append(json.dumps(gt, ensure_ascii=False, indent=2)[:4000])
        lines.append("```")
    else:
        lines.append("_Sem dados de Google Trends (checar token/keywords)._")
    lines += ["", "## Para o editor (Camada 2)",
              "- Etiquetar cada sinal com o pilar que ele serve.",
              "- Filtrar o que é varejo/contradiz o posicionamento premium (vira contraste, não pauta).",
              "- Nunca transformar sinal em promessa de contemplação.", ""]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"  Radar escrito em {path}")

def load_env():
    """Procura um .env subindo a partir deste script (raiz do squad) e carrega no ambiente."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        p = os.path.join(d, ".env")
        if os.path.isfile(p):
            for line in open(p):
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
            return p
        d = os.path.dirname(d)
    return None

def main():
    load_env()
    token = os.environ.get("APIFY_TOKEN")
    if not token or token == "COLAR_O_TOKEN_AQUI":
        sys.exit("APIFY_TOKEN não configurado. Preencha o valor real em squad-marketing/.env.")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    no_trends = "--no-trends" in sys.argv
    only_trends = "--only-trends" in sys.argv
    cfg_path = args[0] if args else "marca/trend-config.json"
    with open(cfg_path) as f:
        cfg = json.load(f)
    stamp = datetime.date.today().strftime("%Y-%m")
    cfg["_stamp"] = stamp
    print(f"Trend Hunter · {cfg.get('cliente','')} · {stamp}")
    ig = [] if only_trends else instagram(cfg.get("instagram_profiles", []), cfg.get("posts_por_perfil", 5), token)
    gt = [] if no_trends else google_trends(cfg.get("google_trends_keywords", []), cfg.get("geo", "BR"), token)
    out = cfg.get("radar_out", f"marca/output/radar/radar-{stamp}.md")
    write_radar(cfg, ig, gt, out)
    # salva bruto pra inspeção
    raw = out.replace(".md", "-raw.json")
    with open(raw, "w") as f:
        json.dump({"instagram": ig, "google_trends": gt}, f, ensure_ascii=False, indent=2)
    print(f"  Bruto em {raw}")

if __name__ == "__main__":
    main()
