# Consts
N_BYTES: int = 2**10
N: int = 71
DIRS: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Check the square is free and unvisited
is_unvisted = lambda x, y : 0 <= y < N and 0 <= x < N and grid[y][x] == '.'

# Build grid
grid: list[list[str]] = [['.']*N for _ in range(N)]

# Read obstacles
for x, y in (tuple(map(int, input().split(','))) for _ in range(N_BYTES)):
    grid[y][x] = '#'

# BFS
Q: list[tuple[int, int, int]] = [(0, 0, 0)]
ptr: int = 0
while ptr < len(Q):
    # Pop from queue
    x, y, d = Q[ptr]
    ptr += 1

    # Check element still unvisited
    if not is_unvisted(x, y): continue
    grid[y][x] = 'O'

    # Finish if arrived to exit
    if (y, x) == (N - 1, N - 1):
        print(d)
        exit(0)
    
    # Visit neighbours
    for dx, dy in DIRS:
        Q.append((x + dx, y + dy, d + 1))
