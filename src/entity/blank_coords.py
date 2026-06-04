"""Blank cell coordinates — 1-index, row-major scan."""

from entity.constants import BLANK_CELL, GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return (row, col) pairs for blank cells, 1-indexed, row-major order."""
    coords: list[tuple[int, int]] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            if grid[row_index][col_index] == BLANK_CELL:
                coords.append((row_index + 1, col_index + 1))
    return coords
