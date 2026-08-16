INFO 521 handouts
=================

Committed copies of the six student-facing hub pages, rendered to PDF and DOCX
for upload to D2L. These are snapshots, not the source of truth. The source is
the matching .qmd one directory up:

  syllabus.qmd    -> syllabus.pdf    syllabus.docx
  schedule.qmd    -> schedule.pdf    schedule.docx
  assessment.qmd  -> assessment.pdf  assessment.docx
  projects.qmd    -> projects.pdf    projects.docx
  discussions.qmd -> discussions.pdf discussions.docx
  homeworks.qmd   -> homeworks.pdf   homeworks.docx

Why this folder exists
----------------------
Quarto writes these same files into _site/ through the format-links mechanism,
so the published site serves them at gchism94.github.io/info521/<page>.pdf.
But _site/ is gitignored, so nothing there survives a clean checkout. This
folder is the tracked copy: it is what you hand to D2L, and what someone
cloning the repo can read without running a render.

Each page also has a standalone HTML beside it (same stem, .html): a
self-contained D2L version with no navbar, math pre-rendered to MathML (no
scripts, no CDN), and every internal link rewritten to the published hub URL.
Upload it as a D2L content-topic FILE; do not paste into the WYSIWYG editor.

Regenerating
------------
  quarto render
  cp _site/{syllabus,schedule,assessment,projects,discussions,homeworks}.{pdf,docx} handouts/
  python tools/build_d2l_html.py     # the standalone D2L .html versions

Do that whenever a .qmd changes, or the two drift apart. The renders here were
produced with Quarto 1.6.40, US Letter, Arial 10.5pt, UA navy headings.

Formatting notes
----------------
PDF goes through Typst. DOCX uses reference.docx in the repo root for its
styles. Both are configured per page in the .qmd front matter, so a change to
one page's look does not silently move the others.
