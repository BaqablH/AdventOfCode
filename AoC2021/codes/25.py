def gen(M):
    n, m = len(M), len(M[0])
    def can_move_right(M, i, j):
        return M[i][j] == '>' and M[i][(j + 1)%m] == '.'
    def can_move_down(M, i, j):
        return M[i][j] == 'v' and M[(i + 1)%n][j] == '.'
    def get_value_right(M, i, j):
        return 'v' if M[i][j] == 'v' else '.' if can_move_right(M, i, j) else '>' if can_move_right(M, i, j - 1) else M[i][j]
    def get_value_down(M, i, j):
        return '>' if M[i][j] == '>' else '.' if can_move_down(M, i, j) else 'v' if can_move_down(M, i - 1, j) else M[i][j]
    def update_right(M):
        return [[get_value_right(M, i, j) for j in range(m)] for i in range(n)]
    def update_down(M):
        return [[get_value_down(M, i, j) for j in range(m)] for i in range(n)]
    def update(M):
        return update_down(update_right(M))
    yield M
    while True:
        N = update(M)
        if N == M:
            return
        yield N
        M = N

l = list(gen(open('../inputs/25.inp').read().splitlines()))
print(len(l))