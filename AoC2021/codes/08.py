from itertools import permutations

data = list(line.replace(' | ', ' ').split() for line in open('../inputs/08.inp'))
conv = {x : i for i, x in enumerate(['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'])}

def solve(line):
    for perm in permutations('abcdefg'):
        perm_map = dict(zip(perm, 'abcdefg'))
        if all(map(lambda y : ''.join(sorted(y)) in conv, ((perm_map[c] for c in w) for w in line))):
            return sum(x*10**i for i, x in enumerate(conv[''.join(sorted(y))] for y in [(perm_map[c] for c in w) for w in line[13:9:-1]]))

print(sum(sum(len(x) in [2, 3, 4, 7] for x in line[10:]) for line in data))
print(sum(map(solve, data)))
