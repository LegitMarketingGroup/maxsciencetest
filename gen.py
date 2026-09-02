"""Generate the online quiz from content.py.  One source of truth, no drift."""
import json, re, content as C

def strip_count(q):
    """Online version does not tell him how many are correct."""
    return re.sub(r"\s*Circle all (five|six|four|that apply)\.?\s*$", " Select all that apply.", q).strip()

DATA = {
    "matchTerms": C.MATCHING_TERMS + C.ONLINE_MATCH_DECOYS,
    "match": [[d, t] for d, t in C.MATCHING_ITEMS],
    "mc": [{"q": s, "o": o, "a": a} for s, o, a in C.MULTIPLE_CHOICE],
    "fillBank": C.FILL_WORD_BANK + C.ONLINE_FILL_DECOYS,
    "fill": [{"t": t, "a": a} for t, a in C.FILL_IN],
    "tf": [{"t": t, "v": v, "why": w} for t, v, w in C.TRUE_FALSE],
    "chart": [[r[0], r[1], r[2]] for r in C.CHART_ROWS],
    "chartExample": list(C.CHART_EXAMPLE),
    "chartBank": C.CHART_WORD_BANK,
    "levels": C.CLASSIFICATION_LEVELS,
    "levelBank": C.LEVEL_WORD_BANK,
    "mnemonic": C.CLASSIFICATION_MNEMONIC,
    "short": [
        ({"type": "multi", "q": strip_count(s["q"]), "n": s["n"],
          "options": [[t, ok] for t, ok in s["options"]]} if s["type"] == "multi" else
         {"type": "order", "q": s["q"], "steps": s["steps"]} if s["type"] == "order" else
         {"type": "mc", "q": s["q"], "options": s["options"], "a": s["a"]})
        for s in C.SHORT_ANSWER
    ],
    "xmc": [{"q": s, "o": o, "a": a} for s, o, a in C.ONLINE_EXTRA_MC],
    "xtf": [{"t": t, "v": v, "why": w} for t, v, w in C.ONLINE_EXTRA_TF],
}

# no banned characters anywhere in the content
blob = json.dumps(DATA, ensure_ascii=False)
for ch, name in {"—": "em dash", "–": "en dash", "~": "tilde"}.items():
    assert ch not in blob, "found " + name

tpl = open("template.html", encoding="utf-8").read()
assert tpl.count("/*__CONTENT__*/") == 1
artifact = tpl.replace("/*__CONTENT__*/", json.dumps(DATA, ensure_ascii=False, indent=None))
open("quiz.html", "w", encoding="utf-8").write(artifact)

# full standalone document for GitHub
i = artifact.index("<header")
doc = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<meta name="description" content="LCA 7th grade Life Science Chapter 1 practice quiz for Max. '
       'Multiple choice, true/false and word bank only, graded instantly.">\n'
       + artifact[:i].strip()
       + '\n<style>img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
       + artifact[i:].strip() + '\n</body>\n</html>\n')
open("index.html", "w", encoding="utf-8").write(doc)

pts = dict(A=len(C.MATCHING_ITEMS), B=len(C.MULTIPLE_CHOICE),
           C=sum(len(a) for _, a in C.FILL_IN), D=len(C.TRUE_FALSE),
           E=2 * len(C.CHART_ROWS), F=len(C.CLASSIFICATION_LEVELS),
           G=3 * len(C.SHORT_ANSWER), H=len(C.ONLINE_EXTRA_MC) + len(C.ONLINE_EXTRA_TF))
print("online parts:", pts, "total", sum(pts.values()))
print("wrote quiz.html", len(artifact), "and index.html", len(doc))
