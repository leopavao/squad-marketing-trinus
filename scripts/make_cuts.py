#!/usr/bin/env python3
"""Corta trechos do vídeo-fonte (ffmpeg) e gera SRT re-timado por corte."""
import json, os, subprocess, sys

BASE = "/Users/afonsohomer/schnAIder/produtos/squad-marketing/trinus/marca/assets/video"
SRC = f"{BASE}/SWp6KhQrlMk.mp4"
OUTDIR = f"{BASE}/cortes"
os.makedirs(OUTDIR, exist_ok=True)
segs = json.load(open(f"{BASE}/transcript.json"))

# (nome, início, fim)
CUTS = [
    ("corte1-terceiros-pagarem", 162.14, 193.10),
    ("corte2-quem-nao-tem-pressa", 406.26, 441.26),
    ("corte3-credito-imediato",   812.52, 851.80),
]

def srt_ts(t):
    if t < 0: t = 0
    h=int(t//3600); m=int((t%3600)//60); s=t%60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".",",")

for name, a, b in CUTS:
    out_mp4 = f"{OUTDIR}/{name}.mp4"
    # corte re-encodado (preciso, com áudio)
    cmd = ["ffmpeg","-y","-ss",str(a),"-to",str(b),"-i",SRC,
           "-c:v","libx264","-preset","fast","-crf","20",
           "-c:a","aac","-b:a","160k", out_mp4]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    # SRT re-timado
    cues=[]; i=0
    for s in segs:
        if s["end"]>a and s["start"]<b:
            i+=1
            st=max(0, s["start"]-a); en=min(b-a, s["end"]-a)
            cues.append(f"{i}\n{srt_ts(st)} --> {srt_ts(en)}\n{s['text'].strip()}\n")
    with open(f"{OUTDIR}/{name}.srt","w") as f:
        f.write("\n".join(cues))
    dur=b-a
    print(f"{name}: {dur:.1f}s · {i} legendas · {out_mp4}")

print("ok")
