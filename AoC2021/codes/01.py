vals = [int(line.rstrip()) for line in open('../inputs/01.inp', 'r')]
print([sum(b > a for a, b in zip(vals, vals[w:])) for w in [1, 3]])
