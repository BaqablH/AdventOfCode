from functools import lru_cache, reduce

def solve1(p1, p2, d = 0, s1 = 0, s2 = 0, k = 0):
    while s2 < 1000:
        p1, p2, d, s1, s2, k = p2, (p1 + 3*d + 6) % 10, (d + 3) % 100, s2, s1 + 1 + (p1 + 3*d + 6) % 10, k + 3
    return k * s1

@lru_cache(maxsize = None)
def solve2(p1, p2, s1 = 0, s2 = 0):
    return (0, 1) if s2 >= 21 else reduce(
        lambda l, r : (l[0] + r[0]*r[1][1], l[1] + r[0]*r[1][0]),
        list((k, solve2(p2, (p1 + d) % 10, s2, s1 + 1 + (p1 + d) % 10)) for d, k in
                [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]),
        (0, 0))

p1, p2 = [int(l.split()[-1]) - 1 for l in open('../inputs/21.inp')]
print(solve1(p1, p2))
print(max(solve2(p1, p2)))