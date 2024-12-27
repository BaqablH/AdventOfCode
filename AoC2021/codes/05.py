from collections import Counter
from itertools import chain
import numpy as np

# Returns all points of a segment with integer coordinates
# by using convex combinations
def points_in_segment(x1, y1, x2, y2):
    n = max(abs(x1 - x2), abs(y1 - y2))
    return [tuple((np.array([x1, y1])*d + np.array([x2, y2])*(n - d))//n) 
                                                    for d in range(0, n + 1)]

# Solves the problem by looking at how many points are seen at least twice
def solve(line_list):
    print(sum(c > 1 for (_, c) in Counter(chain.from_iterable(
                    points_in_segment(*line) for line in line_list)).items()))

lines = list(map(lambda l : list(
        map(int, l.replace(' -> ', ',').split(','))), open('../inputs/05.inp')))

solve([(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2])
solve(lines)
