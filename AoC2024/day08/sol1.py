import itertools
import sys

grid = [line.strip() for line in sys.stdin.readlines()]
dct = {c : [] for row in grid for c in row if c != '.'}
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c != '.':
            dct[c].append((i, j))
print(len({(X, Y) for positions in dct.values()
                for (x1, y1), (x2, y2) in itertools.permutations(positions, 2)
                    if 0 <= (X := 2*x1 - x2) < (N := len(grid)) and
                       0 <= (Y := 2*y1 - y2) < (M := len(grid[0]))}))
        
