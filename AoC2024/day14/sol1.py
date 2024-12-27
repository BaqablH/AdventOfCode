from functools import reduce
from itertools import product
import math
import re
import sys
from typing import Callable, Tuple

# Constants
N, M = 101, 103
STEPS = 100

# Type Definitions
RobotDescription = Tuple[int, int, int, int]
Position = Tuple[int, int]
QuadrantCount = Tuple[Tuple[int, int], Tuple[int, int]]

# Read a line
read_line: Callable[[str], RobotDescription] = lambda line : tuple(map(int, re.findall(r'-?\d+', line)))

# Given p_i and v_i, get the final P_i coordinate value
get_final_coord: Callable[[int, int], int] = lambda x, p, coord_size : (x + p*STEPS) % coord_size

# Given position and velocity, get the robot's final position
get_final_position: Callable[[RobotDescription], Position] = lambda P : \
    tuple(get_final_coord(*P[i::2], coord_size) for (i, coord_size) in [(0, N), (1, M)])

# Tell if the robot located at Position pos is in Quadrant (i, j). Returns False in the "centered cross"
in_quadrant: Callable[[Position, int, int], bool] = lambda pos, i, j: \
    pos[0] != N//2 and pos[1] != M//2 and (i, j) == (pos[0]//((N + 1)//2), pos[1]//((M + 1)//2))

# Updates the current quadrant count after including the new position
quad_count_counter: Callable[[QuadrantCount, Position], QuadrantCount] = lambda quad_count, pos : \
    tuple(tuple(quad_count[i][j] + in_quadrant(pos, i, j) for j in range(2)) for i in range(2))

# Returns the product of the accumulated quadrant count in each quadrant
get_ans: Callable[[QuadrantCount], int] = lambda Q : math.prod(Q[i][j] for i, j in product(range(2), repeat=2)) 

# Print answer
print(get_ans(reduce(
    quad_count_counter,
    (get_final_position(read_line(line)) for line in sys.stdin.readlines()),
    ((0, 0), (0, 0))
)))