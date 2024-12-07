import functools
import itertools
import sys

# Get lhs of the line and list with the values in the rhs
get_lhs_and_vals = lambda line : (int(line.split(':')[0]), line.split(": ")[1].split())

# Given a list of values and operators, compute the resulting expression
compute_rhs = lambda vals, ops : functools.reduce(
    lambda x, P : int(f"{x}{P[1]}") if P[0] == '|' else
        eval(str(x) + "".join(P)), zip(ops, vals[1:]), int(vals[0])) 

# Return generator with all the possible rhs values
possible_rhs_vals = lambda vals: (compute_rhs(vals, ops)
                                  for ops in itertools.product("+*|", repeat=len(vals) - 1))

# Only print the lhs than have a possible matching rhs
print(sum(lhs for lhs, vals in map(get_lhs_and_vals, sys.stdin.readlines())
          if lhs in possible_rhs_vals(vals)))
