data = list(map(lambda line : line.rstrip().split('-'), open('../inputs/12.inp')))
data += [(y, x) for x, y in data]
graph = {x : [Y for X, Y in data if x == X] for x, _ in data}

def baq(twice, cur = 'start', forb = set()):
    if cur in forb:
        if twice is not False or cur in ['start', 'end']:
            return 0
        twice = True
    forb = set([cur if cur.islower() else None, *forb])
    return 1 if cur == 'end' else sum(baq(twice, x, forb) for x in graph[cur])

print(baq(None))
print(baq(False))