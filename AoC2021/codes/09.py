from itertools import product
from math import prod

# Reads data and stores dimensions
data = list(map(lambda line : list(map(int, line.rstrip())), open('../inputs/09.inp')))
n, m, delta = len(data), len(data[0]), [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Solves part one by checking which positions are local minima
print(sum(data[i][j] + 1 for i, j in product(range(n), range(m)) if all(
    map(lambda P : (not (0 <= i + P[0] < n and 0 <= j + P[1] < m)) or data[i][j] < data[i + P[0]][j + P[1]], delta))))

# Returns size of a connected component made out of numbers < 9, and sets all its elements to 9
def dfs(x, y):
    data[x][y] = 9 
    return 1 + sum(dfs(x + i, y + j) for i, j in delta if 0 <= x + i < n and 0 <= y + j < m and data[x + i][y + j] != 9)

# Solves part two by computing all connected components and multiplying the sizes of the 3 largest ones
print(prod(sorted(dfs(i, j) for i, j in product(range(n), range(m)) if data[i][j] != 9)[:-4:-1]))
