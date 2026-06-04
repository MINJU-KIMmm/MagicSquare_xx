"""Shared pytest fixtures — data only, no domain logic."""

import pytest

from entity.constants import BLANK_CELL, GRID_SIZE


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
