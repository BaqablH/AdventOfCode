import itertools
import numpy as np
import re
import sys
from typing import Callable, Optional, Iterator

MAX_VAL: int = 101

# Generator to read lines. Artificially adds enough Nones at the end to stop itertools.takewhile 
read_line: Iterator[Optional[str]] = itertools.chain((line if line else None for line in sys.stdin), [None]*5)

# Converts a string to a tuple containing the numbers included in it
get_numbers_in_line: Callable[[str], np.array] = lambda line : np.array(list(map(int, re.findall(r'-?\d+', line))))

# Finds the minimum score given base vectors and goal, returns 0 if no solution
solve = lambda v, w, goal: min(
    (3*a + b for a in range(MAX_VAL) for b in range(MAX_VAL) if np.array_equal(a*v + b*w, goal)),
    default=0)

# Sums over the different cases
print(sum(solve(*map(get_numbers_in_line, P[:3])) for P in itertools.takewhile(
    lambda P : any(x is not None for x in P),
    (tuple(next(read_line) for _ in range(4)) for __ in itertools.count()))))