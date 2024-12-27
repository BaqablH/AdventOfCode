lines = open('../inputs/20.inp').read().splitlines()

def Solve(data, rep, marg, n, m):
    is_lit = lambda M, x, y, bg : lines[0][
        int(''.join('01'[M[X][Y] if 0 <= X < n and 0 <= Y < m else bg]
                    for X in [x-1,x,x+1] for Y in [y-1,y,y+1]), 2)] == '#'
    update = lambda M, k, bg : M if k == 0 else update(
                    [[is_lit(M, i, j, bg) for j in range(m)] for i in range(n)], k - 1, lines[0][-bg] == '#')
    extended_matrix = lambda : [[marg <= i < n-marg and marg <= j < m-marg and data[i-marg][j-marg] == '#'
                        for j in range(m)] for i in range(n)]
    return sum(x for line in update(extended_matrix(), rep, False) for x in line)

solve = lambda M, rep : Solve(M, rep, rep + 1, len(M) + 2*rep + 2, len(M[0]) +  2*rep + 2)
print(*(solve(lines[2:], k) for k in [2, 50]), sep='\n')
