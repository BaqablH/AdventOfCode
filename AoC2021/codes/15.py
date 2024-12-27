from queue import PriorityQueue as PQ

# Dijkstra algorithm
def dijkstra(cave):
    n = len(cave)
    dist = [[0 if (i, j) == (0, 0) else 10**9 for j in range(n)] for i in range(n)]
    pq = PQ()
    pq.put((0, 0, 0))
    
    def update(d, X, Y):
        if 0 <= X < n and 0 <= Y < n and d + cave[X][Y] < dist[X][Y]:
            dist[X][Y] = d + cave[X][Y]
            pq.put((d + cave[X][Y], X, Y))

    def iterate(d, x, y):
        if d == dist[x][y]:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                update(d, x + dx, y + dy) 

    while not pq.empty():
        iterate(*pq.get())
           
    return dist[-1][-1]

augment = lambda minicave, n : [[(minicave[i%n][j%n] + i//n + j//n - 1)%9 + 1
                                        for j in range(5*n)] for i in range(5*n)]

data = [list(map(int, l.rstrip())) for l in open('../inputs/15.inp')]
print(dijkstra(data))
print(dijkstra(augment(data, len(data))))
