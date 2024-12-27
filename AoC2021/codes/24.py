lines = open('../inputs/24.inp').read().splitlines()
d, a, b = map(lambda k : [int(l.split()[-1]) for l in lines[k::18]], [4, 5, 15])

sols = []
def baqtracking(z = 0, sol = 0, p = 0):
    if z == 0 and p > 0:
        sols.append(sol)
    if p == 14:
        return
    if d[p] == 1:
        for w in range(1, 10):
            baqtracking(26*z + w + b[p], 10*sol + w, p + 1)
    elif 1 <= (z % 26) + a[p] <= 9:
            baqtracking(z // 26, 10*sol + (z % 26) + a[p], p + 1)

baqtracking()

print(sols[-1])
print(sols[0])
