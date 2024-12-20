import itertools
import sys

DIRS: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
THRESHOLD: int = 100
MAX_CHEAT_DIST: int = 20

# Read racetrack
racetrack: list[list[str]] = list(list(x.strip()) for x in sys.stdin.readlines())

# Finds starting position
x, y = next((i, j) for i, row in enumerate(racetrack) for j, c in enumerate(row) if c == 'S')

# Mark every position from start to end with a number 
for i in itertools.takewhile(lambda _ : x is not None, itertools.count()):
    racetrack[x][y] = i
    x, y = next(((x + dx, y + dy) for dx, dy in DIRS if racetrack[x + dx][y + dy] in ['.', 'E']), (None, None))

# Find the number of cheats that save at least the threshold
print(sum(1 for x, y in itertools.product(range(1, len(racetrack) - 1), range(1, len(racetrack) - 1))
            for delta_x in range(max(-x, -MAX_CHEAT_DIST), min(len(racetrack) - x, MAX_CHEAT_DIST + 1))
            for delta_y in range(max(-y, -MAX_CHEAT_DIST + abs(delta_x)), min(len(racetrack[0]) - y, MAX_CHEAT_DIST - abs(delta_x) + 1)) if
                racetrack[x][y] != '#' and racetrack[x + delta_x][y + delta_y] != '#' and
                racetrack[x + delta_x][y + delta_y] - racetrack[x][y] - abs(delta_x) - abs(delta_y) >= THRESHOLD))
          

