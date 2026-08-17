# INFO 521: Machine Learning Foundations, the course hub

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21971088.svg)](https://doi.org/10.5281/zenodo.21971088)

If using these course materials, cite the following:
>Chism, G. (2026). INFO 521: Machine Learning Foundations — Course Hub (Version v1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21971088

The public, evergreen hub site for INFO 521, a 7.5-week graduate course
(University of Arizona, College of Information Science). This repo renders to the
course website: schedule, syllabus, assessment model, homework unit pages, project
pages, discussions, readings.

It is the center of a five-repo course. The spokes:

| Repo | Visibility | Carries |
|---|---|---|
| `info521-slides-2026` | public | lecture decks, module overview decks, recording scripts, D2L note pages |
| `info521-activities-2026` | public | six interactive peer-loop tools |
| `info521-projects-2026` | public | the two-part project: milestone notebooks, data loader, briefs |
| `info521-homeworks-2026` | **private** | homework source of truth and all instructor material (solutions, quiz banks, keys) |

**Instructors: start with `INSTRUCTOR_CHECKLIST.md` in the private homeworks repo.**
It walks the full GitHub organization + Classroom 50 setup. Nothing in this hub repo
creates repos, pushes, or wires Classroom 50; all remote operations are manual.

## What is in this repo

```
_variables.yml       the single source for spoke URLs; edit this to roll the hub to a new term
_quarto.yml          site config (navbar, footer, theme, published resources)
theme.scss           UA branding, light/dark
index.qmd            landing page
schedule.qmd         the module-by-module table (the centerpiece)
syllabus.qmd         full syllabus: outcomes, weights (55/25/10/9/1), policies
assessment.qmd       how grading works: specifications, bundles, the homework ladder
homeworks.qmd        the seven homework deliverables, best five count
homeworks/           per-unit pages, single-sourced from the private homeworks repo's intros/
projects.qmd         one project, two parts, nine milestones, gates
activities.qmd       the peer-engagement loop model and tool links
discussions.qmd      the weekly discussion prompts and quality bar
slides.qmd           deck index
readings/            open-licensed PDF excerpts served with the site
handouts/            instructor handouts (not published as site resources by default)
reference.docx       Word reference for DOCX renders of site pages
Course_Map_INFO521.docx/.pdf   the course map document for D2L
.github/workflows/publish.yml  GitHub Pages deploy (Settings → Pages → Source: GitHub Actions)
```

The `homeworks/_unit*.qmd` files are folded, byte-identical copies of
`info521-homeworks-2026/intros/_unit*.qmd`. Edit them there, not here; the two sets
are kept in lockstep (14 file pairs).

## Rendering

Quarto 1.4+.

```bash
quarto preview        # local preview
quarto render         # renders to _site/ (gitignored; Pages builds via Actions)
```

## Rolling to a new term

The hub has no year in its name. To roll forward: point `_variables.yml` at the new
term's dated spoke repos, update any changed weeks in `schedule.qmd`, push. Course
content on this site is week-paced (no fixed calendar dates), so most terms need no
other edit.
