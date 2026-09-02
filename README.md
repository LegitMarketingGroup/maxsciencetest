# Max's LCA Life Science Chapter 1 Quiz

An interactive practice quiz for BJU Press Life Science, Chapter 1: God's Living World (sections 1.1 through 1.9),
styled to Lexington Christian Academy.

- **83 questions, 102 points.** Every one is multiple choice, true/false, or picked from a word bank. No typing.
- **Graded instantly**, with the correct answer and a short explanation on anything missed.
- **90% or higher:** fireworks and a cheer. Anything less: a womp womp and a very large fart.
- Progress and best score are saved in the browser.

## Harder than the paper version

The printable practice test is 71 questions and 90 points. This online version adds four things the paper
copy cannot do:

1. A **Challenge Round** (Part H) of 12 extra questions that are not on the PDF.
2. **Bigger word banks** with more decoy terms, so elimination helps less.
3. **Select-all questions do not say how many are correct.**
4. **Answer choices reshuffle on every attempt**, so retaking it cannot be passed by memorizing letter positions.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole quiz, one self-contained file |
| `content.py` | Every question and answer, the single source of truth |
| `template.html` | Page shell and logic, with the content injected at build time |
| `gen.py` | Builds `index.html` from `content.py` + `template.html` |
| `build.py` | Builds the two PDFs: practice test and a separate answer key |

Change a question in `content.py`, run `python3 gen.py && python3 build.py`, and the online quiz, the printed
test, and the answer key all update together.

## Run it

Open `index.html` in any browser, or use the GitHub Pages link for this repo.
