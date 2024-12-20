import itertools
import sys

DIRS: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
THRESHOLD: int = 100

# Read racetrack
racetrack: list[list[str]] = list(list(x.strip()) for x in sys.stdin.readlines())

# Finds starting position
x, y = next((i, j) for i, row in enumerate(racetrack) for j, c in enumerate(row) if c == 'S')

# Mark every position from start to end with a number 
for i in itertools.takewhile(lambda _ : x is not None, itertools.count()):
    racetrack[x][y] = i
    x, y = next(((x + dx, y + dy) for dx, dy in DIRS if racetrack[x + dx][y + dy] in ['.', 'E']), (None, None))

# Find the number of cheats that save at least the threshold
print(sum(1 for x, y, (dx, dy) in itertools.product(range(1, len(racetrack) - 1), range(1, len(racetrack[0]) - 1), DIRS[:2])
            if racetrack[x + dx][y + dy] != '#' and racetrack[x - dx][y - dy] != '#' and
                abs(racetrack[x + dx][y + dy] - racetrack[x - dx][y - dy]) - 2 >= THRESHOLD))