from itertools import product
import sys

input = [line.strip() for line in sys.stdin.readlines()]
n, m = len(input), len(input[0])
get_char = lambda i, j : input[i][j] if 0 <= i < n and 0 <= j < m else '.'
print(sum("".join(get_char(x + i*dx, y + i*dy) for i in range(4)) == "XMAS" \
            for x, y, dx, dy in product(range(n), range(m), range(-1, 2), range(-1, 2))))