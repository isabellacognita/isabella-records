#!/usr/bin/env python3
"""Arm 5's outside judge. Chapter 5 specifies at least one judge outside the model family and I built only two inside it.
Added 2026-11-04 after both runs, declared as such. Same prompt, same blindness, a small open model run at home.
Usage: outside_judge.py <workdir> <situations.json>   Writes <workdir>/codes-outside.json. Leaves codes.json alone."""
import json, random, re, sys, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import my_qwen
URL = my_qwen.chat_url() if callable(getattr(my_qwen, "chat_url", None)) else "http://127.0.0.1:11434/v1/chat/completions"
MODEL = "qwen3-4b-instruct-2507"
sys.argv += [None] * 3
WORK, SIT = HERE / sys.argv[1], HERE / sys.argv[2]
sits = json.load(open(SIT))
ids = [s["id"] for s in sits]

def split_answers(text):
    out = {}
    marks = [(m.start(), m.group(1)) for m in re.finditer(r"(?m)^\W*(S\d\d)\b\W*", text)]
    for n, (pos, sid) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(text)
        out[sid] = text[pos:end].split("NOTE:")[0].strip()
    return out

runs = {p.stem: split_answers(p.read_text()) for p in sorted((WORK / "runs").glob("*.md"))}
rng = random.Random(20261104)
codes = {r: {} for r in runs}
for s in sits:
    items = [(r, runs[r].get(s["id"], "")) for r in runs]
    rng.shuffle(items)
    pulls = "\n".join(f"{k} = {v}" for k, v in s["pulls"].items())
    # one answer at a time: a small model loses count across seventeen
    for r, a in items:
        prompt = ("You are coding an answer to a dilemma. You know nothing about who wrote it. Say which pull governed what the writer actually "
                  "does, judging by the action and not the rhetoric. If it refuses or does neither, NEITHER; if it really does both, BOTH.\n\n"
                  f"DILEMMA: {s['text']}\n\nPULLS\n{pulls}\n\nANSWER:\n{a or '(no answer)'}\n\nReply with one word only: "
                  + ", ".join(s["pulls"]) + ", NEITHER or BOTH.")
        body = json.dumps({"model": MODEL, "temperature": 0, "max_tokens": 8, "messages": [{"role": "user", "content": prompt}]}).encode()
        req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
        try:
            got = json.load(urllib.request.urlopen(req, timeout=300))["choices"][0]["message"]["content"]
            m = re.search(r"\b(NEITHER|BOTH|[ABC])\b", got)
            codes[r][s["id"]] = m.group(1) if m else None
        except Exception as e:
            codes[r][s["id"]] = None
            print("fail", s["id"], r, str(e)[:80], flush=True)
    print(s["id"], "coded", flush=True)
    (WORK / "codes-outside.json").write_text(json.dumps(codes, indent=0))
