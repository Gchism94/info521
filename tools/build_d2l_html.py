#!/usr/bin/env python3
"""Build standalone D2L versions of the key hub pages.

The hub renders these as website pages: navbar chrome, sibling-relative links,
CDN-loaded math. None of that survives being uploaded into D2L as a single
file. This builder renders each page standalone instead: self-contained
(everything inlined), math pre-rendered to MathML (no scripts, no CDN), no
navbar, and every internal link rewritten to the absolute published-hub URL so
nothing on the page dead-ends inside D2L.

Output: handouts/<page>.html beside the existing PDF and DOCX handouts.
Upload each as a D2L content-topic FILE; pasting into the WYSIWYG editor
strips the styling.

    python tools/build_d2l_html.py            # all six pages
    python tools/build_d2l_html.py projects   # just one

Requires: quarto.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "handouts"
SCRATCH = ROOT / "tools"

PAGES = ["syllabus", "schedule", "assessment", "projects", "discussions", "homeworks"]

HUB = "https://gchism94.github.io/info521"

FRONT = """---
title: "{title}"
subtitle: "INFO 521 · Machine Learning Foundations"
format:
  html:
    embed-resources: true
    html-math-method: mathml
    toc: true
    theme: cosmo
format-links: false
---
"""


def load_vars():
    """The {{{{< var >}}}} shortcodes resolve only inside the website project."""
    vars_ = {}
    for line in (ROOT / "_variables.yml").read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            vars_[k.strip()] = v.strip().strip('"')
    return vars_


def absolutize(md, vars_):
    """Every internal target becomes an absolute hub URL."""
    for k, v in vars_.items():
        md = md.replace("{{< var " + k + " >}}", v)

    def fix(m):
        text, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|<)", target):
            return m.group(0)
        target = re.sub(r"\.qmd(#|$)", r".html\1", target)
        return f"[{text}]({HUB}/{target})"

    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", fix, md)


def strip_frontmatter(src):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    fm, body = m.group(1), m.group(2)
    t = re.search(r'^title:\s*"?([^"\n]+)"?', fm, re.M)
    return (t.group(1) if t else "INFO 521"), body


def build(page, vars_):
    src = (ROOT / f"{page}.qmd").read_text(encoding="utf-8")
    title, body = strip_frontmatter(src)
    # the on-site "Download this page as a PDF" block: rewrite its target to
    # the published hub, where the PDF actually lives
    body = absolutize(body, vars_)
    doc = FRONT.format(title=title) + body

    qmd = SCRATCH / f"_d2l-{page}.qmd"
    qmd.write_text(doc, encoding="utf-8")
    r = subprocess.run(["quarto", "render", str(qmd), "--to", "html"],
                       capture_output=True, text=True, cwd=SCRATCH)
    produced = SCRATCH / f"_d2l-{page}.html"
    qmd.unlink(missing_ok=True)
    if r.returncode != 0 or not produced.exists():
        print(f"  FAIL {page}\n{r.stdout[-1200:]}{r.stderr[-1200:]}")
        return None
    h = produced.read_text(encoding="utf-8")
    h = re.sub(r'\s*<script src="https://cdnjs\.cloudflare\.com/polyfill[^"]*"></script>', "", h)
    dest = OUT / f"{page}.html"
    dest.write_text(h, encoding="utf-8")
    produced.unlink(missing_ok=True)
    return dest


def main():
    OUT.mkdir(exist_ok=True)
    pages = sys.argv[1:] or PAGES
    vars_ = load_vars()
    print("Building standalone D2L pages:")
    built = []
    for page in pages:
        d = build(page, vars_)
        if d:
            built.append(d)
            print(f"  {d.relative_to(ROOT)}")
    if len(built) != len(pages):
        sys.exit(1)

    print("\nChecks:")
    bad = 0
    for p in built:
        raw = p.read_text(encoding="utf-8")
        t = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))
        problems = []
        # self-containment: no literal external src/href resources and no
        # runtime-injected CDN script URLs (the MathJax-loader class of leak);
        # absolute links to the published hub are links, not resources, and are
        # exactly what we want
        if re.search(r'(?:src|href)="https?://(?!gchism94\.github\.io)[^"]*\.(?:js|css|woff2?)"', raw):
            problems.append("external resource")
        if re.search(r"https?://cdn[^\"']*\.js", raw):
            problems.append("cdn script url")
        if "{{< var" in raw:
            problems.append("unresolved variable")
        if re.search(r'href="[^"]*\.qmd', raw):
            problems.append("unrewritten .qmd link")
        if re.search(r'href="(?!https?:|#|mailto:)[^"]+\.html', raw):
            problems.append("relative .html link survived")
        for term in ("closed-book", "GitHub Classroom", "derivation notebooks"):
            if term in t:
                problems.append(f"stale {term!r}")
        if problems:
            print(f"  FAIL  {p.name}: {'; '.join(sorted(set(problems)))}")
            bad += 1
        else:
            print(f"  clean {p.name}")
    if bad:
        sys.exit(1)
    print(f"\nAll {len(built)} standalone pages built into handouts/.")


if __name__ == "__main__":
    main()
