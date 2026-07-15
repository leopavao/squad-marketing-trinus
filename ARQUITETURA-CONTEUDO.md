# A casa do conteúdo (arquitetura do squad)

A operação de conteúdo é uma casa. A fundação sustenta tudo; cada camada usa a de baixo.

```
┌─────────────────────────────────────────────────────────┐
│  CAMADA 4 — Distribuição (NÃO AGORA, vender na hora)     │
│  postagem automática nos canais                         │
├─────────────────────────────────────────────────────────┤
│  CAMADA 3 — Execução                                    │
│  produzir a peça (carrossel, story, roteiro de vídeo)   │
│  agentes: diretor-criativo, copywriter, designer (OD)   │
├─────────────────────────────────────────────────────────┤
│  CAMADA 2 — Definição de conteúdo                       │
│  insight -> pauta: qual pilar, qual tema, qual canal,   │
│  qual formato (foto / vídeo / carrossel / story)        │
│  agente: editor-conteudo                                │
├─────────────────────────────────────────────────────────┤
│  CAMADA 1 — Inteligência (insights)                     │
│  o que está em tendência: Instagram + Google Trends     │
│  agente: trend-hunter (via Apify)                       │
├─────────────────────────────────────────────────────────┤
│  FUNDAÇÃO — Editoria (pilares institucionais)           │
│  o cérebro: o que a marca precisa oferecer de conteúdo  │
│  agentes: editor-conteudo + diretor-criativo (perene)   │
└─────────────────────────────────────────────────────────┘
```

## O que cada nível faz

- **Fundação (Editoria):** define os pilares institucionais. Perene, revisita trimestral. Saída: `output/pilares-de-conteudo.md`.
- **Camada 1 (Inteligência):** o trend-hunter puxa sinal real do Instagram (concorrentes/referências) e do Google Trends (keywords), via Apify. Saída: `output/radar/radar-AAAA-MM.md`.
- **Camada 2 (Definição):** o editor cruza pilares + radar + contrato de operação e define as pautas do ciclo (tema, pilar, canal, formato). Saída: `output/editoria/calendario-AAAA-MM.md`.
- **Camada 3 (Execução):** diretor + copy + designer produzem cada peça (no Open Design). Saída: `output/<peça>`.
- **Camada 4 (parada):** postagem automática. Não construir agora.

## Configs que sustentam a casa

- `marca/contrato-operacao.md` — canais, formatos, cadência (lido pela Camada 2).
- `marca/watchlist.md` + `trend-config.json` — fontes do trend-hunter (lido pela Camada 1).
