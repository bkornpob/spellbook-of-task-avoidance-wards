#!/usr/bin/env python3
"""Single markdown page → mp3 via Piper LJSpeech-high @ 1.5x.

Usage:
    python3.10 tts_single_page.py <input.md> <output.mp3>
"""
import re, os, subprocess, sys

sys.path.insert(0, "/home/bkornpob/.local/lib/python3.10/site-packages")
from piper.voice import PiperVoice
from piper.config import SynthesisConfig
import wave

if len(sys.argv) < 3:
    print("usage: tts_single_page.py <input.md> <output.mp3>")
    sys.exit(1)

MD = sys.argv[1]
OUT = sys.argv[2]
VOICE = "/home/bkornpob/.hermes/hermes-agent/en_US-ljspeech-high.onnx"
SPEED = 1.5

os.makedirs(os.path.dirname(OUT), exist_ok=True)

txt = open(MD, "r", encoding="utf-8").read()

# strip frontmatter
if txt.startswith("---\n"):
    m = re.match(r"^---\n[\s\S]*?^---\n\n", txt, flags=re.MULTILINE)
    if m:
        txt = txt[m.end():]

# clean markdown for speech
txt = re.sub(r"<!--.*?-->", "", txt, flags=re.DOTALL)
txt = re.sub(r"!\[.*?\]\(.*?\)", "", txt)
txt = re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1", txt)
txt = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", txt)
txt = re.sub(r"[*_`#>]+", "", txt)
# convert markdown tables to readable text rows instead of deleting them
def md_table_to_text(txt):
    lines = txt.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # detect table row: starts with |, has content cells, ends with |
        if line.startswith('|') and line.endswith('|') and not all(c in '|-: ' for c in line):
            # collect contiguous table rows (including header + separator)
            rows = []
            j = i
            while j < len(lines) and lines[j].strip().startswith('|') and lines[j].strip().endswith('|'):
                row_line = lines[j].strip()
                # skip separator lines like | --- | --- |
                if not all(c in '|-: ' for c in row_line):
                    cells = [c.strip() for c in row_line.strip('|').split('|')]
                    cells = [c for c in cells if c]  # remove empty from stray splits
                    if cells:
                        rows.append(cells)
                j += 1
            # emit rows as numbered text
            for idx, cells in enumerate(rows, 1):
                out.append(f"row {idx}: {', '.join(cells)}")
            i = j
        else:
            out.append(lines[i])
            i += 1
    return '\n'.join(out)

txt = md_table_to_text(txt)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip()

print(f"chars: {len(txt)}")

voice = PiperVoice.load(VOICE)
sc = SynthesisConfig(length_scale=1.0 / SPEED)
chunks = list(voice.synthesize(txt, syn_config=sc))

audio = bytearray()
for c in chunks:
    audio.extend(c.audio_int16_bytes)

wav_tmp = OUT.replace(".mp3", ".wav")
with wave.open(wav_tmp, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(22050)
    w.writeframes(audio)

subprocess.run(
    ["ffmpeg", "-y", "-i", wav_tmp,
     "-codec:a", "libmp3lame", "-qscale:a", "2", OUT],
    check=True, capture_output=True
)
os.remove(wav_tmp)
size = os.path.getsize(OUT)
print(f"ok → {OUT} ({size:,} bytes)")
