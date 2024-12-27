vals = list(map(int, open('../inputs/07.inp').read().rstrip().split(',')))
print(min(sum(map(lambda y : abs(x - y), vals)) for x in vals))
print(min(sum(map(lambda y : abs(x - y)*(abs(x - y) + 1)//2, vals)) for x in range(min(vals), max(vals))))
