#!/usr/bin/env python3
"""Transcreve um áudio com faster-whisper. Saída: SRT + JSON de segmentos (start, end, text)."""
import sys, json
from faster_whisper import WhisperModel

audio = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"
out_base = sys.argv[2] if len(sys.argv) > 2 else audio.rsplit(".", 1)[0]

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

print("carregando modelo small (int8)...", flush=True)
model = WhisperModel("small", device="cpu", compute_type="int8")
print("transcrevendo...", flush=True)
segments, info = model.transcribe(audio, language="pt", vad_filter=True)

segs = []
srt = []
for i, s in enumerate(segments, 1):
    segs.append({"i": i, "start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()})
    srt.append(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n")
    if i % 20 == 0:
        print(f"  ...{i} segmentos ({s.end:.0f}s)", flush=True)

with open(out_base + ".srt", "w") as f:
    f.write("\n".join(srt))
with open(out_base + ".json", "w") as f:
    json.dump(segs, f, ensure_ascii=False, indent=1)
print(f"OK: {len(segs)} segmentos. {out_base}.srt e {out_base}.json", flush=True)
