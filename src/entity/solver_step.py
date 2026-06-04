"""Solver step A — int[6] solution for two blanks (entity, no E00x)."""

from entity.blank_coords import find_blank_coords
from entity.constants import BLANK_CELL, TARGET_SUM


def solve_step_a(grid: list[list[int]]) -> list[int]:
    """
    Step A: fill each blank so its row sums to TARGET_SUM.
    Returns [r1, c1, n1, r2, c2, n2] — 1-index, row-major blank order.
    """
    coords = find_blank_coords(grid)
    solution: list[int] = []
    for row_1, col_1 in coords:
        row = grid[row_1 - 1]
        row_sum_filled = sum(cell for cell in row if cell != BLANK_CELL)
        value = TARGET_SUM - row_sum_filled
        solution.extend([row_1, col_1, value])
    return solution


def format_step_a_golden(solution: list[int], *, error_code: str = "") -> str:
    """Fixed golden text: int[6] 1-index + optional error code line."""
    if len(solution) != 6:
        raise ValueError("solution must be int[6]")
    fields = ",".join(str(x) for x in solution)
    lines = [
        "status: success",
        "track: entity",
        "test_id: D-SOL-01",
        f"solution_int6: {fields}",
        f"error_code: {error_code}",
    ]
    return "\n".join(lines) + "\n"
