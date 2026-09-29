# Predictive Complaint Risk Intelligence Platform

Predict a meaningful outcome of a consumer complaint using only information that would be available at prediction time. The source data is the [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/). The exact prediction target will be chosen after the data is explored.

This repository is an ML engineering project: an installable package, tested path configuration, and separate modules for data, features, models, and evaluation. Notebooks stay exploratory. Code the project depends on lives in the package and is covered by tests.

## Planned architecture

Work moves in one direction, and each stage keeps its own files:

1. **Raw data** lands in `data/raw/` unchanged.
2. **Interim data** in `data/interim/` holds cleaned tables that are still broader than the modeling set.
3. **Processed data** in `data/processed/` holds the train, validation, and test tables used for fitting and scoring.
4. **Features** are transforms fit on training rows only, then applied to later splits.
5. **Models** train on those features and write fitted objects to `artifacts/`.
6. **Evaluation** scores held-out data and records metrics next to the model that produced them.

Code for those stages will live under `src/complaint_risk/` in the packages `data`, `features`, `models`, and `evaluation`. Shared path logic lives in `config.py`.

FastAPI (serving a prediction) and MLflow (experiment tracking) are planned for later phases.

## Project structure

```text
.
├── README.md
├── pyproject.toml          # package metadata, dependencies, pytest, Ruff
├── .gitignore
├── .env.example            # template only; no secrets
├── data/
│   ├── raw/                # original downloads, not committed
│   ├── interim/            # cleaned tables, not committed
│   └── processed/          # modeling tables, not committed
├── notebooks/              # exploration only
├── src/
│   └── complaint_risk/     # installable package
│       ├── config.py       # repository-relative paths
│       ├── data/
│       ├── features/
│       ├── models/
│       ├── evaluation/
│       └── utils/
├── tests/
├── artifacts/              # fitted models and metrics, not committed
└── docs/
```

The Python package is `complaint_risk`. The installable project name is `complaint-risk`.

## Current status

Repository foundation only.

- Package layout, path configuration, Ruff, and pytest are in place.
- Dataset ingestion, feature pipelines, model training, and the API are later phases.
- pandas, NumPy, scikit-learn, matplotlib, pydantic, joblib, and python-dotenv are part of the intended stack. Each one is added to `pyproject.toml` when a module first imports it. Seaborn, FastAPI, and MLflow wait until a later phase needs them.

## Setup

Requires Python 3.11 or newer. On this Mac, `/usr/bin/python3` is 3.9 and will not work. Homebrew Python 3.12 is a valid interpreter (`python3.12`).

From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If `python3.12` is not on your `PATH`:

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

`-e ".[dev]"` installs the package in editable mode and installs the development tools (pytest and Ruff).

Copy `.env.example` to `.env` only when you need local settings. Nothing in the foundation reads `.env` today, and `.env` must not be committed.

## Development checks

```bash
ruff check .
ruff format --check .
pytest
```

`ruff format .` rewrites files that fail the format check.
