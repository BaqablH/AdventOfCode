from typing import List, Tuple, Set, Callable
import sys
from functools import reduce

Coordinate = Tuple[int, int]
SuperCoordinate = Tuple[int, int, int, int]

DIRS: List[Coordinate] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid: List[List[int]] = list(map(lambda line : list(map(int, line.strip())), sys.stdin.readlines()))

is_interesting: Callable[[int, int, int], bool] = lambda i, j, c : 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == c
interesting_after_translate: Callable[[Set[SuperCoordinate], int, int, int], Set[SuperCoordinate]] = lambda S, dx, dy, c: set({
    (x0, y0, X, Y) for (x0, y0, X, Y) in map(lambda P : (P[0], P[1], P[2] + dx, P[3] + dy), S) if is_interesting(X, Y, c)})

def find_all(pos : Set[Coordinate], lev: int = 1) -> int:
    if (lev > 9): return len(pos)
    return find_all(reduce(
        lambda lhs_set, dir : lhs_set.union(interesting_after_translate(pos, dir[0], dir[1], lev)),
        DIRS,
        set()), lev + 1)
    

print(find_all({(i, j, i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == 0}))
