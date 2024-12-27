from itertools import product

line = open('../inputs/17.inp').read()
line = ''.join(x if x in '-0123456789' else ' ' for x in line)
l, r, b, u = map(int, line.strip().split())

def attempt(P):
    x, y, vx, vy, mxy, ok = 0, 0, *P, 0, False
    while not (x > r or (y < b and vy < 0)):
        x, y, vx, vy, mxy, ok = x + vx, y + vy, max(0, vx - 1), vy - 1, max(y + vy, mxy), ok or (l <= x <= r and b <= y <= u)
    return ok, mxy

L = [mxy for ok, mxy in map(attempt, product(range(r + 1), range(-abs(b), abs(b) + 1))) if ok]

print(max(L), len(L), sep='\n')