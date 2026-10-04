#!/usr/bin/env python3
"""Copy the practice files from TutorNotes into Quartz's content folder,
turning every ```tikz block into a pre-rendered SVG image.

Usage: python3 scripts/publish_tutornotes.py <TutorNotes folder> <content folder>
Needs pdflatex (with tikz + standalone) and pdftocairo (poppler-utils).
"""
import hashlib, os, re, shutil, subprocess, sys, tempfile

# Files to publish: path inside TutorNotes -> (folder in content, image prefix)
FILES = [
    ("Physics 240/Exam Drop-in Sessions/Physics240Exam2-Practice-Problems.md", "Exam Drop-in Sessions", "problems"),
    ("Physics 240/Exam Drop-in Sessions/Physics240Exam2-Practice-Worked.md", "Exam Drop-in Sessions", "worked"),
]

PREAMBLE = r"""\documentclass[border=8pt]{standalone}
\usepackage{tikz}\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,calc,angles,quotes,decorations.pathmorphing,patterns}
\begin{document}
\pagecolor{white}
"""

def render(code, svg_path, build_dir):
    # Labels drawn white for Obsidian's dark theme become black on the white card
    code = code.replace("text=white", "text=black").replace("[white]", "[black]")
    name = hashlib.sha1(code.encode()).hexdigest()[:12]
    tex = os.path.join(build_dir, name + ".tex")
    with open(tex, "w", encoding="utf-8") as f:
        f.write(PREAMBLE + code + "\n\\end{document}\n")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", build_dir, tex], capture_output=True, text=True)
    if r.returncode != 0:
        errs = [l for l in r.stdout.splitlines() if l.startswith("!")]
        raise SystemExit(f"TikZ failed for {svg_path}: {errs[:3]}")
    subprocess.run(["pdftocairo", "-svg", os.path.join(build_dir, name + ".pdf"), svg_path], check=True)

def convert(src_file, out_dir, prefix, build_dir):
    diag_dir = os.path.join(out_dir, "diagrams")
    os.makedirs(diag_dir, exist_ok=True)
    lines = open(src_file, encoding="utf-8").read().split("\n")
    out, i, example, k, count, section, used = [], 0, "top", 0, 0, 0, set()
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            section += 1
        m = re.match(r"^## Example (\S+)", line)
        if m:
            example, k = m.group(1), 0
            if "-" not in example:  # "Example 1" -> "1-1" so sections don't overwrite each other
                example = f"{section}-{example}"
        if line.startswith("```tikz"):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            k += 1; count += 1
            svg = f"{prefix}-{example}-{k}.svg"
            while svg in used:  # never let two diagrams share a file name
                svg = svg[:-4] + "b.svg"
            used.add(svg)
            render("\n".join(lines[i + 1:j]), os.path.join(diag_dir, svg), build_dir)
            out.append(f"![Example {example} diagram](diagrams/{svg})")
            i = j + 1
            continue
        out.append(line)
        i += 1
    dest = os.path.join(out_dir, os.path.basename(src_file))
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(out))
    print(f"{os.path.basename(src_file)}: {count} diagrams")

def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    notes, content = sys.argv[1], sys.argv[2]
    build_dir = tempfile.mkdtemp()
    cleaned = set()
    for rel, folder, prefix in FILES:
        out_dir = os.path.join(content, folder)
        if out_dir not in cleaned:  # start fresh so deleted diagrams don't linger
            shutil.rmtree(os.path.join(out_dir, "diagrams"), ignore_errors=True)
            cleaned.add(out_dir)
        convert(os.path.join(notes, rel), out_dir, prefix, build_dir)

if __name__ == "__main__":
    main()
