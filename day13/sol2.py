import itertools
import re
import sys
from typing import Callable, Optional, Iterator, Tuple

Pair = Tuple[int, int]

MAX_VAL: int = 101
DELTA = 10000000000000

# Generator to read lines. Artificially adds enough Nones at the end to stop itertools.takewhile 
read_line: Iterator[Optional[str]] = itertools.chain((line if line else None for line in sys.stdin), [None]*5)

# Converts a string to a tuple containing the numbers included in it
get_numbers_in_line: Callable[[str], Pair] = lambda line, delta = 0: \
    tuple(map(lambda x : int(x) + delta, re.findall(r'-?\d+', line)))

# Manually "pre-solves" the equation a*v + b*w == goal, by returning (det, det*a, det*b):
get_det_and_unscaled_solution: Callable[[Pair, Pair, Pair], Tuple[int, int, int]] = lambda v, w, goal: \
    (v[0]*w[1] - w[0]*v[1], *(w[1]*goal[0] - w[0]*goal[1], -v[1]*goal[0] + v[0]*goal[1]))

# From the integer values (det, det*a, det*b), checks whether a and b are integers
# Returns 3*a + b in that case, and 0 otherwise
solve: Callable[[int, int, int], Tuple[int, int, int]] = lambda det, unscaled_sol_x, unscaled_sol_y: \
    (3*unscaled_sol_x + unscaled_sol_y)//det if all(x % det == 0 for x in [unscaled_sol_x, unscaled_sol_y]) else 0

# Sums over the different cases
print(sum(
    solve(
        *get_det_and_unscaled_solution(get_numbers_in_line(v), get_numbers_in_line(w), get_numbers_in_line(goal, DELTA)))
    for v, w, goal, _ in itertools.takewhile(
        lambda P : any(x is not None for x in P),
        (tuple(next(read_line) for _ in range(4)) for __ in itertools.count()))))