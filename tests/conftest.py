"""Shared pytest fixtures — data only, no domain logic."""

import importlib.util
from pathlib import Path

import pytest

_CONSTANTS_PATH = Path(__file__).resolve().parent.parent / "src" / "entity" / "constants.py"
_spec = importlib.util.spec_from_file_location("entity_constants", _CONSTANTS_PATH)
assert _spec and _spec.loader
_constants = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_constants)
BLANK_CELL = _constants.BLANK_CELL
GRID_SIZE = _constants.GRID_SIZE


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1: 4×4, blank cells (0) at (2,2) and (3,3) — 1-index, row-major order."""
    grid = [
        [1, 2, 3, 4],
        [5, BLANK_CELL, 7, 8],
        [9, 10, BLANK_CELL, 12],
        [13, 14, 15, 16],
    ]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    return grid
