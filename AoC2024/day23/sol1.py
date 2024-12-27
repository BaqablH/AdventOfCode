from collections import defaultdict
from itertools import combinations
import sys

# Build graph by reading the input
G = defaultdict(set)
for lhs, rhs in (edge.strip().split('-') for edge in sys.stdin.readlines()):
    G[lhs].add(rhs)
    G[rhs].add(lhs)

# Generate potential triplets. Keep them sorted to filter repetitions later
potential_triplets = (tuple(sorted((a, b, c))) for a in G if a.startswith('t') for b, c in combinations(G[a], 2) if c in G[b])

# Rrint how many unique ones we got
print(len(set(potential_triplets)))

