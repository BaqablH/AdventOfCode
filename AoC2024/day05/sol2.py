import functools
import itertools
import sys

N = 100
input = [line.strip() for line in sys.stdin.readlines()]
graph = [[False]*N for _ in range(N)]
split_by_char = lambda c : \
    map(lambda line : list(map(int, line.split(c))), filter(lambda line : c in line, input)) 

for i, j in split_by_char("|"):
    graph[i][j] = True

print(
    sum(
        map(
            lambda L : L[len(L)//2],
            map(
                lambda L : sorted(
                    L, key=functools.cmp_to_key(lambda i, j: -1 if graph[i][j] else int(graph[j][i]))
                ),
                filter(lambda L : any(graph[y][x] for x, y in itertools.combinations(L, 2)),
                       split_by_char(",")
                )
            )
        )
    )
)