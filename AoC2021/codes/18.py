from functools import reduce
from copy import deepcopy

size = lambda L : 1 if isinstance(L, int) else size(L[0]) + size(L[1])
ispair = lambda L : isinstance(L, list) and isinstance(L[0], int) and isinstance(L[1], int)

# Returns first position of explosion (if any) and exploding pair
def find_explode(L, depth = 1, k = 0):
    if isinstance(L, list):
        if depth == 4:
            if ispair(L[0]): return k, *L[0]
            if ispair(L[1]): return k + 1, *L[1]
        P = find_explode(L[0], depth + 1, k)
        return find_explode(L[1], depth + 1, k + size(L[0])) if P is None else P

# Returns list after explosion
def explode(L, p, sl, sr, k = 0):
    if isinstance(L, int):
        if k in [p - 1, p + 1]:
            return L + (sl if k == p - 1 else sr)
        return L
    update_explode = lambda L, k : 0 if k == p and ispair(L) else explode(L, p, sl, sr, k)
    L[0] = update_explode(L[0], k)
    L[1] = update_explode(L[1], k + size(L[0]))
    return L

# Splits list if needed
def split(L):
    if isinstance(L, int):
        return (L, False) if L < 10 else ([L//2, (L + 1)//2], True)
    L[0], was_split = split(L[0])
    if was_split:
        return L, True
    L[1], was_split = split(L[1])
    return L, was_split

# Performs all explosions and split required for list L
def simplify(L):
    P = find_explode(L)
    if P is not None:
        return simplify(explode(L, *P))
    L, was_split = split(L)
    return simplify(L) if was_split else L

add = lambda l, r : simplify([deepcopy(l), deepcopy(r)])
magnitude = lambda L : L if isinstance(L, int) else 3*magnitude(L[0]) + 2*magnitude(L[1])

data = list(map(eval, open('../inputs/18.inp')))
print(magnitude(reduce(add, data)))
print(max(magnitude(add(x, y)) for x in data for y in data if x is not y))
