import sys
from typing import List, Tuple, Callable, Generator
from functools import reduce
from math import prod

Pair = Tuple[int, int]

DIRS: List[Pair] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid: List[str] = [line.strip() for line in sys.stdin.readlines()]
N, M = len(grid), len(grid[0])
visited: List[List[bool]] = [[False]*M for _ in range(N)]

def dfs(x: int, y: int) -> Pair:
    """Returns a pair of ints for the area and perimeter found during the exploration"""
    if (visited[x][y]): return (0, 0)
    visited[x][y] = True

    is_ours: Callable[[int, int], bool] = lambda X, Y: 0 <= X < N and 0 <= Y < M and grid[x][y] == grid[X][Y]

    # Sum (areas, perimeters) found in exploration.
    # Add 1 to the area for this element and 1 for each non-ours adjacent elements
    return reduce(
        lambda lhs, rhs: (lhs[0] + rhs[0], lhs[1] + rhs[1]),    # Element-wise sum
        (dfs(X, Y) if is_ours(X, Y) else (0, 1) for X, Y in ((x + dx, y + dy) for dx, dy in DIRS)), (1, 0))

print(sum(prod(dfs(i, j)) for i in range(N) for j in range(M)))
