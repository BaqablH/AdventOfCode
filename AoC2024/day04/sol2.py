from itertools import product
import sys

DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
VALID_COMBINATIONS = ["MMSS"[i:] + "MMSS"[:i] for i in range(4)]
input = [line.strip() for line in sys.stdin.readlines()]
n, m = len(input), len(input[0])
get_char = lambda i, j : input[i][j] if 0 <= i < n and 0 <= j < m else '.'

print(sum(input[x][y] == 'A' and
        "".join(get_char(x + dx, y + dy) for dx, dy in DIRS) in VALID_COMBINATIONS
            for x, y, dir in product(range(n), range(m), range(1, 2))))