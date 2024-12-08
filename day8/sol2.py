import itertools
import sys

grid = [line.strip() for line in sys.stdin.readlines()]
N, M = len(grid), len(grid[0])
dct = {c : [] for row in grid for c in row if c != '.'}
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c != '.':
            dct[c].append((i, j))

print(len(
    {(X, Y)
        for positions in dct.values()
            for (x1, y1), (x2, y2) in itertools.permutations(positions, 2)
                for X, Y in itertools.takewhile(
                    lambda P : 0 <= P[0] < N and 0 <= P[1] < M, 
                    map(
                        lambda i : (x1 + i*(x2 - x1), y1 + i*(y2 - y1)),
                        itertools.count()
                    ))}))
        
