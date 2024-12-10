from typing import List, Tuple, Callable, Counter as Ctr
import sys
from collections import Counter
from functools import reduce

Coordinate = Tuple[int, int]

DIRS: List[Coordinate] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid: List[List[int]] = list(map(lambda line : list(map(int, line.strip())), sys.stdin.readlines()))

is_interesting: Callable[[int, int, int], bool] = lambda i, j, c : 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == c
interesting_after_translate: Callable[[Ctr[Coordinate], int, int, int], Ctr[Coordinate]] = lambda C, dx, dy, c: Counter({
    (x + dx, y + dy) : ctr for (x, y), ctr in C.items() if is_interesting(x + dx, y + dy, c)})

def find_all(pos : Ctr[Coordinate], lev: int = 1):
    if (lev > 9): return sum(pos.values())
    return find_all(reduce(
        lambda lhs_set, dir : lhs_set + interesting_after_translate(pos, dir[0], dir[1], lev),
        DIRS,
        Counter()), lev + 1)
    

print(find_all(Counter((i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == 0)))
