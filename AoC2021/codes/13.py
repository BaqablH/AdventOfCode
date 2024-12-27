from functools import reduce
from operator import indexOf, itemgetter

# Reads data, splits into points and instructions
data = open('../inputs/13.inp').read().splitlines()
points = set(tuple(map(int, s.split(','))) for s in data[:indexOf(data, '')])
ins = [(z, int(p)) for z, p in map(lambda s : s[11:].split('='), data[indexOf(data, '')+1:])]

# Updates set of points pts after instruction i
update = lambda pts, i: set((i[1] - abs(i[1] - x), y) if i[0] == 'x' else (x, i[1] - abs(i[1] - y)) for x, y in pts)

# Returns matrix given by set of points
range2matrix = lambda pts, x, y : '\n'.join(''.join(' #'[(a, b) in pts] for a in range(x)) for b in range(y))
set2matrix = lambda pts : range2matrix(pts, max(map(itemgetter(0), pts)) + 1, max(map(itemgetter(1), pts)) + 1)

print(len(update(points, ins[0])))
print(set2matrix(reduce(update, ins, points)))
