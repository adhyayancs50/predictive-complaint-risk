"""Repository paths.

Defaults are derived from the directory that contains ``pyproject.toml``.
The search starts at this file, so the result does not depend on the
process working directory and no machine-specific path is hardcoded.
"""

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    """Walk parent directories until ``pyproject.toml`` is found.

    Args:
        start: File or directory to start from. Defaults to this module's path.

    Returns:
        Absolute path to the repository root.

    Raises:
        FileNotFoundError: If no parent directory contains ``pyproject.toml``.
    """
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent

    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").is_file():
            return candidate

    raise FileNotFoundError(
        "Could not find the repository root. "
        "Expected pyproject.toml in a parent of the starting path."
    )


REPO_ROOT = find_repo_root()

DATA_DIR = REPO_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
ARTIFACTS_DIR = REPO_ROOT / "artifacts"
