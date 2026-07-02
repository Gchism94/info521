# INFO 521 — Evergreen Course Hub

**Machine Learning Foundations** (7.5-week graduate course)

This repository is the central hub for INFO 521. It surfaces the module-by-module schedule and links out to three spoke repositories:

- [`info521-slides-2026`](https://github.com/gchism94/info521-slides-2026) — Lecture decks in Quarto + reveal.js
- [`info521-activities-2026`](https://github.com/gchism94/info521-activities-2026) — Six weekly peer-engagement loops
- [`info521-homeworks-2026`](https://github.com/gchism94/info521-homeworks-2026) — GitHub Classroom assignment template (private)

## Rendering Locally

**Prerequisites**: Quarto 1.4+ (https://quarto.org/docs/get-started/)

```bash
# Preview in browser (http://localhost:3000)
quarto preview

# Render to _site/
quarto render

# Render without committing to git
quarto render --to html
```

## Evergreen Rollover

This hub is **evergreen** — it has no year in its name and always points to the current term's dated spokes. To roll forward to the next term:

1. Edit [`_variables.yml`](_variables.yml) to update the three spoke URLs (e.g., `info521-slides-2027`, `info521-activities-2027`, etc.)
2. Commit and push
3. The hub automatically reflects the new spoke URLs — no code changes needed

All schedule content (readings, topics, module descriptions) is generated from each spoke's structure, so spokes can evolve independently.

## Remote Operations

All remote operations are **manual** (performed by Greg):

- Repository creation and initial setup on GitHub
- Pushing changes to remote (`git push`)
- Enabling GitHub Pages and configuring the publish workflow
- Creating GitHub Classroom assignment and invite links

### Optional: Publishing Workflow

A GitHub Actions workflow (`.github/workflows/publish.yml`) is included but **not active** by default. To enable auto-publish to GitHub Pages:

1. Push the hub to GitHub
2. Go to **Settings → Pages**
3. Set **Source** to "GitHub Actions"
4. The workflow will run on every push and deploy to `https://gchism94.github.io/info521`

Alternatively, publish locally with:
```bash
quarto publish gh-pages
```

## File Structure

```
_variables.yml              Central spoke URLs (single source of truth)
_quarto.yml                 Website config (navbar, footer, theme)
theme.scss                  UA branding (navy, red, light/dark)
index.qmd                   Landing page with three cards
schedule.qmd                Module-by-module table (THE centerpiece)
activities.qmd              Peer-loop model explained + tool links
slides.qmd                  Deck index + rendering instructions
assessment.qmd              Grading scheme, projects, checkpoints
README.md                   This file
.github/workflows/publish.yml  Optional GitHub Pages deploy workflow
```

## Team

- **Instructor**: Greg Chism
- **Email**: gchism94@gmail.com
- **Institution**: University of Arizona, School of Information
