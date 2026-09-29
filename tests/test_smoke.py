"""Smoke test: the package imports, and project paths resolve inside the repo."""

import complaint_risk
from complaint_risk.config import (
    ARTIFACTS_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
    REPO_ROOT,
    find_repo_root,
)


def test_package_imports() -> None:
    assert complaint_risk.__version__ == "0.1.0"


def test_project_paths_resolve_inside_repository() -> None:
    assert (REPO_ROOT / "pyproject.toml").is_file()
    assert find_repo_root(RAW_DATA_DIR) == REPO_ROOT

    assert RAW_DATA_DIR == REPO_ROOT / "data" / "raw"
    assert INTERIM_DATA_DIR == REPO_ROOT / "data" / "interim"
    assert PROCESSED_DATA_DIR == REPO_ROOT / "data" / "processed"
    assert ARTIFACTS_DIR == REPO_ROOT / "artifacts"

    for path in (RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR, ARTIFACTS_DIR):
        assert path.is_dir()
        assert path.is_absolute()
        assert path.is_relative_to(REPO_ROOT)
