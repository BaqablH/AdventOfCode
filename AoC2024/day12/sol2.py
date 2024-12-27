import sys
from typing import List, Tuple, Callable
from functools import reduce
from math import prod

Pair = Tuple[int, int]

DIRS: List[Pair] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid: List[str] = [line.strip() for line in sys.stdin.readlines()]
N, M = len(grid), len(grid[0])
visited: List[List[bool]] = [[False]*M for _ in range(N)]

sum_pairs: Callable[[Pair, Pair], Pair] = lambda lhs, rhs: (lhs[0] + rhs[0], lhs[1] + rhs[1])

def dfs(x: int, y: int) -> Pair:
    """Returns a pair of ints for the area and perimeter found during the exploration"""
    if (visited[x][y]): return (0, 0)
    visited[x][y] = True

    neighbors: List[Pair] = [(x + dx, y + dy) for dx, dy in DIRS]

    is_ours: Callable[[int, int], bool] = lambda X, Y: 0 <= X < N and 0 <= Y < M and grid[x][y] == grid[X][Y]
    makes_convex_corner: Callable[[Pair, Pair], bool] = lambda pos1, pos2: not is_ours(*pos1) and not is_ours(*pos2)
    makes_concave_corner: Callable[[Pair, Pair], bool] = lambda pos1, pos2: is_ours(*pos1) and is_ours(*pos2) and not is_ours(*reduce(sum_pairs, [pos1, pos2], (-x, -y)))
    makes_corner: Callable[[Pair, Pair], bool] = lambda pos1, pos2: makes_convex_corner(pos1, pos2) or makes_concave_corner(pos1, pos2)

    # Sum (areas, perimeters) found in exploration
    # Add (area of 1, number of "border" sides) in current element
    return reduce(
        sum_pairs,
        (dfs(X, Y) for X, Y in neighbors if is_ours(X, Y)),
        (1, sum(1 for N1, N2 in zip(neighbors, neighbors[1:] + [neighbors[0]]) if makes_corner(N1, N2))))

print(sum(prod(dfs(i, j)) for i in range(N) for j in range(M)))
