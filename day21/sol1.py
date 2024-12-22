from itertools import combinations
from functools import cache
import sys

# Number of intermediate robots
LEVELS = 2

KEYBOARD_LAYOUT = [" ^A", "<v>"]
DISPLAY_LAYOUT = ["789", "456", "123", " 0A"]

# Map each character to its position
build_button_map = lambda layout : {c : (i, j) for i, row in enumerate(layout) for j, c in enumerate(row) if c != ' '}

KEYBOARD_BUTTON_MAP = build_button_map(KEYBOARD_LAYOUT)
DISPLAY_BUTTON_MAP = build_button_map(DISPLAY_LAYOUT)

MOVEMENT_TO_DIR = {'^' : (-1, 0), '<' : (0, -1), 'v' : (1, 0), '>' : (0, 1)}

# Check if a path only goes through valid poiitions
def path_is_valid(x, y, path, positions):
    for dx, dy in (MOVEMENT_TO_DIR[move] for move in path):
        x, y = x + dx, y + dy
        if (x, y) not in positions: return False
    return True

@cache
def compute(start, end, level = 0):
    # Compute path description info
    button_map = DISPLAY_BUTTON_MAP if level == 0 else KEYBOARD_BUTTON_MAP
    x0, y0 = button_map[start]
    x1, y1 = button_map[end]
    abs_x_delta, abs_y_delta = abs(x1 - x0), abs(y1 - y0)

    # Return if last level reached
    if level == LEVELS: return abs_x_delta + abs_y_delta + 1

    vertical_dir = 'v' if x1 > x0 else '^'
    horizontal_dir = '>' if y1 > y0 else '<'

    # Will be given by get_kth_char_in_combination(comb)(k)
    get_kth_char_in_combination = lambda comb : lambda k : vertical_dir if k in comb else horizontal_dir

    # Generate paths
    path_combinations = (combinations(range(abs_x_delta + abs_y_delta), abs_x_delta))
    generate_paths = ("".join(map(get_kth_char_in_combination(comb), range(abs_x_delta + abs_y_delta))) for comb in path_combinations)

    # Computes path length by backtracking one level above based of every pair of consecutives charactes
    compute_path_length = lambda path : sum(compute(l, r, level + 1) for l, r in zip(path, path[1:]))
    return min(compute_path_length('A' + path + 'A') for path in generate_paths if path_is_valid(x0, y0, path, button_map.values()))

solve_case = lambda buttons: sum(compute(p0, p1) for p0, p1 in zip('A' + buttons, buttons))

if __name__ == "__main__":
    print(sum(solve_case(line) * int(line.removesuffix('A')) for line in map(lambda line : line.strip(), sys.stdin.readlines())))
