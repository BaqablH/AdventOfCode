from functools import reduce
from itertools import product
import math
import re
import sys
from typing import Callable, Tuple, List

# Constants
N, M = 101, 103
MAX_STEPS: int = N * M

# Type Definitions
RobotDescription = Tuple[int, int, int, int]
Position = Tuple[int, int]
QuadrantCount = Tuple[Tuple[int, int], Tuple[int, int]]

# Read a line
read_line: Callable[[str], RobotDescription] = lambda line : tuple(map(int, re.findall(r'-?\d+', line)))
robot_descriptions: List[RobotDescription] = list(map(read_line, sys.stdin.readlines()))

def create_image(steps):
    # Given p_i and v_i, get the final P_i coordinate value
    get_final_coord: Callable[[int, int], int] = lambda x, p, coord_size : (x + p*steps) % coord_size

    # Given position and velocity, get the robot's final position
    get_final_position: Callable[[RobotDescription], Position] = lambda P : \
        tuple(get_final_coord(*P[i::2], coord_size) for (i, coord_size) in [(0, N), (1, M)])
    
    # Create image
    image = [[' ']*M for _ in range(N)]
    for x, y in map(get_final_position, robot_descriptions):
        image[x][y] = 'X'

    # Store ASCII image
    with open(f"day14/image_{steps}.txt", "w") as img:
        for row in image:
            img.write("".join(row))
            img.write("\n")

# These values come from looking at pattern in the first 200s:
# Images after 25, 62, 128 and 163 seem interesting
for steps in range(MAX_STEPS):
    if steps%103 == 25 and steps%101 == 62:
        create_image(steps)
    
