import sys

# Consts
N: int = 71
DIRS: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Read input
inp: list[tuple[int, int]] = list(tuple(map(int, line.strip().split(','))) for line in sys.stdin.readlines())

def has_solution(n_bytes: int) -> bool:
    # Build grid
    grid: list[list[str]] = [['.']*N for _ in range(N)]

    # Read obstacles
    for x, y in inp[:n_bytes]:
        grid[y][x] = '#'

    # Check the square is free and unvisited
    is_unvisted = lambda x, y : 0 <= y < N and 0 <= x < N and grid[y][x] == '.'

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

        # If arrived to exit, there is a solution
        if (y, x) == (N - 1, N - 1):
            return True
        
        # Visit neighbours
        for dx, dy in DIRS:
            Q.append((x + dx, y + dy, d + 1))

    # If BFS ended without finding the solution, return False
    return False

# Binary search to find the solution
L, R = 0, len(inp)
while R > L + 1:
    M = (L + R)//2
    if has_solution(M): L = M
    else: R = M

# Print answer
print(*inp[L], sep=',')
