# ACEest Fitness & Gym — DevOps Assignment (Flask adaptation)

This repository contains a simple Flask web API adapted from a provided local workout tracker. It demonstrates core DevOps practices required for the assignment: Git + GitHub, Pytest unit tests, Docker containerization, and a GitHub Actions CI workflow.

## Repository contents
- `app.py` — Flask application (workout tracking endpoints)
- `requirements.txt` — Python dependencies
- `tests/test_app.py` — Pytest test suite
- `Dockerfile` — Containerizes the app
- `.github/workflows/ci.yml` — GitHub Actions workflow to build and test on push/PR
- `README.md`, `.gitignore`

## Setup and run locally

### Using Python (recommended for quick testing)
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# App available at http://127.0.0.1:5000
```

### Using Docker
```bash
docker build -t aceest-fitness:local .
docker run --rm -p 5000:5000 aceest-fitness:local
```

## Running tests locally
```bash
pytest -q
```

## CI/CD (GitHub Actions)
On every push or pull request the workflow will:
1. Install dependencies and run `pytest` on the runner.
2. Build the Docker image.
3. Run `pytest` inside the built Docker image.

## Notes for submission
- Create a **public** GitHub repository and push these files.
- Confirm that Actions are visible under the **Actions** tab and show successful runs for recent commits.
- Provide the repository URL as your submission.
