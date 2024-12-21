from itertools import combinations
from functools import cache
import sys

LEVELS = 2

KEYBOARD_BUTTON_MAP = {
    '^' : (0, 1),
    'A' : (0, 2),
    '<' : (1, 0),
    'v' : (1, 1),
    '>' : (1, 2),
}

DISPLAY_BUTTON_MAP = {
    '7' : (0, 0),
    '8' : (0, 1),
    '9' : (0, 2),
    '4' : (1, 0),
    '5' : (1, 1),
    '6' : (1, 2),
    '1' : (2, 0),
    '2' : (2, 1),
    '3' : (2, 2),
    '0' : (3, 1),
    'A' : (3, 2),
}

MOVEMENT_TO_DIR = {
    '^' : (-1, 0),
    '<' : (0, -1),
    'v' : (1, 0),
    '>' : (0, 1),
}

def check_valid(x, y, path, positions):
    for dx, dy in (MOVEMENT_TO_DIR[move] for move in path):
        x, y = x + dx, y + dy
        if (x, y) not in positions: return False
    return True

@cache
def compute(start, end, level = 0):
    button_map = DISPLAY_BUTTON_MAP if level == 0 else KEYBOARD_BUTTON_MAP
    x0, y0 = button_map[start]
    x1, y1 = button_map[end]
    dx, dy = x1 - x0, y1 - y0
    cx = 'v' if dx > 0 else '^'
    cy = '>' if dy > 0 else '<'
    n_movs = abs(dx) + abs(dy)
    if level == LEVELS: return n_movs + 1
    generate_paths = ("".join(cx if i in comb else cy for i in range(n_movs)) for comb in combinations(range(n_movs), abs(dx)))
    return min(sum(compute(l, r, level + 1) for l, r in zip('A' + path, path + 'A')) for
                path in generate_paths if check_valid(x0, y0, path, button_map.values()))
            
def solve(buttons):
    return sum(compute(p0, p1) for p0, p1 in zip('A' + buttons, buttons))

solve_case = lambda buttons: sum(compute(p0, p1) for p0, p1 in zip('A' + buttons, buttons))
print(sum(solve_case(line) * int(line.removesuffix('A')) for line in map(lambda line : line.strip(), sys.stdin.readlines())))

def test(input, exp):
    ans = compute(*input)
    if (ans == exp): print(f"Case {input}: OK")
    else : print(f"Case {input}: expected {exp}, got {ans}")

test(('A', 'v', 2), 3)
test(('v', '<', 2), 2)
test(('<', '<', 2), 1)
test(('<', 'A', 2), 4)

test(('A', '>', 2), 2)
test(('>', '>', 2), 1)
test(('>', '^', 2), 3)
test(('^', 'A', 2), 2)

test(('A', '<', 1), 10)
test(('<', 'A', 1), 8)
