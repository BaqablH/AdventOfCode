from itertools import chain, product

# Updates matrix from step n to step n + 1
def update(matrix):
    sum_neighbours = lambda i, j: sum(matrix[x + i][y + j] > 9
                        for x, y in product((-1, 0, 1), (-1, 0, 1))
                                if 0 <= x + i < 10 and 0 <= y + j < 10)

    return matrix if sum(x > 9 for x in chain.from_iterable(matrix)) == 0 else \
        update([[matrix[i][j] + sum_neighbours(i, j) if 1 <= matrix[i][j] <= 9 \
                                else 0 for j in range(10)] for i in range(10)])

# Generates steps
def gen():
    matrix = [list(map(int, line.rstrip())) for line in open('../inputs/11.inp')]
    while sum(map(sum, matrix)) > 0:
        yield matrix
        matrix = update([[x + 1 for x in row] for row in matrix])

print(sum(x == 0 for m in list(gen())[:101] for x in chain.from_iterable(m)))
print(len(list(gen())))
