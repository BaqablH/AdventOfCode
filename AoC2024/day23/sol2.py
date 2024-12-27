from collections import defaultdict
from functools import reduce
import sys

# Build graph by reading the input
G = defaultdict(set)
for lhs, rhs in (edge.strip().split('-') for edge in sys.stdin.readlines()):
    G[lhs].add(rhs)
    G[rhs].add(lhs)

get_longest_string = lambda lhs, rhs: lhs if len(lhs) > len(rhs) else rhs

def get_largest_clique_backtracking_str(current_clique: str) -> str:
    # Intersect the neighbours of the elements in the current clique
    intersect_neighbours = reduce(lambda S, x : S & G[x], current_clique.split(','), set(G.keys()))

    # Only the ones larger than the largest element (last two characters) are interesting
    next_elem_candidates = filter(lambda x : x > current_clique[-2:], intersect_neighbours)

    # Return the largest clique we can get among the candidates, return the current one if there's none
    return reduce(
        get_longest_string,
        (get_largest_clique_backtracking_str(current_clique + f",{x}") for x in next_elem_candidates),
        current_clique)
    

print(reduce(get_longest_string, map(get_largest_clique_backtracking_str, G.keys()), ""))
