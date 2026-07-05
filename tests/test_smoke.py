from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

MODULES = ["basics", "chile", "data", "games", "gui", "math", "stats"]


def test_repo_has_readme():
    assert (REPO_ROOT / "README.md").exists()


def test_repo_has_gitignore():
    assert (REPO_ROOT / ".gitignore").exists()


def test_repo_has_license():
    assert (REPO_ROOT / "LICENSE").exists()


@pytest.mark.parametrize("module", MODULES)
def test_module_dirs_exist(module):
    assert (REPO_ROOT / module).is_dir()


def test_scripts_importable():
    for py_file in REPO_ROOT.rglob("*.py"):
        if "pytest" not in py_file.name and "__init__" not in py_file.name:
            rel = py_file.relative_to(REPO_ROOT)
            assert py_file.stat().st_size > 0, f"{rel} está vacío"
