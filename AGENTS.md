**Agent Guidance for english_hub**

This file provides concise, actionable instructions and links to help AI coding agents quickly work with this Django/Wagtail project. Keep edits minimal and link to existing docs rather than copying them.

**Quick Start**

- **Install:** Python virtual environment, then `pip install -r requirements.txt`.
- **Run (dev):** `python manage.py runserver` (uses `hub_site/settings/dev.py`).
- **Run tests:** `python manage.py test`.
- **Migrate:** `python manage.py migrate` then `python manage.py makemigrations` when changing models.
- **Docker (prod):** `docker build -t english_hub .` then run container with appropriate env vars and migrations applied.

**Project Layout (key files)**

- **Django CLI:** [manage.py](manage.py)
- **Dependencies:** [requirements.txt](requirements.txt)
- **Settings:** [hub_site/settings/base.py](hub_site/settings/base.py), [hub_site/settings/dev.py](hub_site/settings/dev.py), [hub_site/settings/production.py](hub_site/settings/production.py)
- **Main app:** [home/](home/) — models and templates ([home/models.py](home/models.py), [home/templates/home](home/templates/home))
- **Search:** [search/views.py](search/views.py)
- **URL routing:** [hub_site/urls.py](hub_site/urls.py)
- **Migrations:** [home/migrations/](home/migrations/)

**Important Notes & Conventions**

- The project uses Django with Wagtail CMS. Treat Wagtail page models and StreamFields carefully when editing content models.
- Database is SQLite (`db.sqlite3`) in the repo. Developers commonly use a local venv (`venv`).
- Static files are collected to `/static/`; production uses `ManifestStaticFilesStorage` — update references using `collectstatic`.
- Media files live in `/media/` and are served directly only in `DEBUG` mode.
- Tests live under app `tests.py` files (e.g., [home/tests.py](home/tests.py)). Run `python manage.py test` to validate changes.

**Claude-specific guidance**

- When generating content or changelogs targeted for Claude-based agents, keep prompts concise and explicit.
- Prefer short, structured outputs (bulleted lists, concise diffs, file paths) so Claude can parse and act on them reliably.
- For code patches, provide unified diffs or an `apply_patch`-style snippet and reference exact files by path.

**When to escalate to a human**

- Destructive DB migrations or schema refactors that require data migrations or manual inspection.
- Changes that affect production settings, secrets, or Docker configuration.

**Next suggested customizations**

- Add a `.github/copilot-instructions.md` linking to this file and providing CI/run instructions.
- Create small skills for common tasks: `run-tests`, `create-migration`, `collect-static`.
