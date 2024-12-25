from collections import defaultdict
import itertools
import sys

LAST_BIT: int = 45

# Read input
first_input_section = itertools.takewhile(lambda line : line, (input().strip() for _ in itertools.count()))
input_bits: dict[str, bool] = {var : (val == "1") for var, val in map(lambda line: line.split(': '), first_input_section)}
deps: dict[str, tuple[str, str, str]] = {res : (lhs, op, rhs)
                                         for lhs, op, rhs, _, res in map(lambda line : line.strip().split(), sys.stdin.readlines())}

# Store the descendants of each key
descendants = defaultdict(list)
for key, (lhs, _, rhs) in deps.items():
    descendants[lhs].append(key)
    descendants[rhs].append(key)

# Given each dependency, tell if the key is misplaced
# Not aiming to solve every possible input but the given one
def is_misplaced(key: str, lhs: str, op: str, rhs: str) -> bool:
    parents_are_decimal: bool = lhs[1:].isdecimal() and rhs[1:].isdecimal()
    misformed_z_key: bool = key[0] == 'z' and key[1:].isdecimal() and op != "XOR" and not (op == "OR" and key == f"z{LAST_BIT}")
    xor_has_unexpected_descendant: bool = \
        op == "XOR" and any(deps[d][1] == 'OR' or (deps[d][1] == 'XOR' and d[1:].isdecimal() and not parents_are_decimal) for d in descendants[key])
    and_has_unexpected_descendant: bool = \
        op == "AND" and {lhs, rhs} != {"x00", "y00"} and any(deps[d][1] != 'OR' for d in descendants[key])
    return any((misformed_z_key, xor_has_unexpected_descendant, and_has_unexpected_descendant))

print(",".join(sorted(key for key, val in deps.items() if is_misplaced(key, *val))))
