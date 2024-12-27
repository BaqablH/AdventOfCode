from queue import Queue
import numpy as np
from itertools import product
from collections import Counter

## Util functions to transform between tuple and matrix

def mat2tuple(M):
    return tuple(M[i, j] for i in range(4) for j in range(4))

def tuple2mat(a):
    return np.matrix(list(list(a[i:i+4] for i in range(0, 16, 4)))).astype(int)

def vec2tuple(v):
    return tuple(v[i,0] for i in range(4))

# Basic rotations
id4 = tuple2mat((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1))
rx = tuple2mat((1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1))
ry = tuple2mat((0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1))
rz = tuple2mat((0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1))

# Build list of rotations
rotations = list(map(tuple2mat, set(mat2tuple(a*b*c*d) for a, b, c, d in product([id4, rx, ry, rz], repeat=4))))

# Read data
lines = open('../inputs/19.inp').read().splitlines()
data = []
for line in lines:
    if '---' in line:
        data.append([])
    elif line:
        data[-1].append(np.array([list(map(int, line.split(','))) + [1]]).T)

# Builds affine transformation matrix consisting of rotation rot and displacement d
def affinemat(rot, d):
    return tuple2mat(tuple(rot[i//4, i%4] if i not in [3, 7, 11] else -d[i//4] for i in range(16)))

coords = [id4 if i == 0 else None for i in range(len(data))]

# Build coords (coords[i] is the transformation matrix to convert ref frame 0 to ref frame i)
Q = Queue()
Q.put(0)
while not Q.empty():
    i = Q.get()
    for j in range(len(data)):
        if coords[j] is None:
            for rot in rotations:
                d, t = Counter(vec2tuple(a - b) for a in [rot * x for x in data[i]] for b in data[j]).most_common()[0]
                if t == 12:
                    coords[j] = affinemat(rot, d)*coords[i]
                    Q.put(j)

print(len(set(vec2tuple(np.linalg.inv(p).astype(int)*x) for i, p in enumerate(coords) for x in data[i])))
print(max(sum(abs(A[0, i] - B[0, i]) for i in range(3)) for A, B in product(
                [np.linalg.inv(p).astype(int)[:, 3].T for p in coords], repeat=2)))
