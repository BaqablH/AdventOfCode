import itertools
import sys

N = 100
input = [line.strip() for line in sys.stdin.readlines()]
graph = [[False]*N for _ in range(N)]
split_by_char = lambda c : \
    map(lambda line : list(map(int, line.split(c))), filter(lambda line : c in line, input)) 

for i, j in split_by_char("|"):
    graph[i][j] = True

print(sum(L[len(L)//2] for L in split_by_char(",") if \
          not any(graph[y][x] for x, y in itertools.combinations(L, 2))))