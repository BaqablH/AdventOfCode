from functools import reduce
from operator import methodcaller

def reducer1(P, Q):
    h, d, instr, x = P + Q
    return {
        "forward" : (h + x, d),
        "down" : (h, d + x),
        "up" : (h, d - x),
    }[instr]

def reducer2(P, Q):
    h, d, a, instr, x = P + Q
    return {
        "forward" : (h + x, d + a*x, a),
        "down" :  (h, d, a + x),
        "up" : (h, d, a - x),
    }[instr]

def solution(reducer, init):
    data = map(lambda l : (l[0], int(l[1])),
                map(methodcaller('split'), open('../inputs/02.inp')))
    a, b = reduce(reducer, data, init)[:2]
    return a*b

print(solution(reducer1, (0, 0)))
print(solution(reducer2, (0, 0, 0)))
