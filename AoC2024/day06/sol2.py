import sys

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
maze = [line.strip() for line in sys.stdin.readlines()]
N, M, K = len(maze), len(maze[0]), len(DIRS)
sys.setrecursionlimit(N*M*K)
is_valid = lambda x, y : 0 <= x < N and 0 <= y < M
x, y = next((i, j) for i, row in enumerate(maze) for j, c in enumerate(row) if c == '^') 

def success(i, j):
    graph = [[[False for k in range(K)] for j in range(M)] for i in range(N)] 
    can_move = lambda x, y, k: not is_valid(x, y) or (maze[x][y] != '#' and (x, y) != (i, j))
    def transverse(x, y, dir):
        if not is_valid(x, y):
            return False
        if graph[x][y][dir]:
            return True
        graph[x][y][dir] = True
        for k in map(lambda j : (j + dir)%4, range(4)):
            dx, dy = DIRS[k]
            X, Y = x + dx, y + dy
            if can_move(X, Y, k):
                return transverse(X, Y, k)
    return transverse(x, y, 0)

print(sum(success(i, j) for i in range(N) for j in range(M) if maze[i][j] == '.'))
