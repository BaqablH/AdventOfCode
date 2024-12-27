from functools import cache, reduce
import itertools
import operator
import sys

# Read input
first_input_section = itertools.takewhile(lambda line : line, (input().strip() for _ in itertools.count()))
input_bits: dict[str, bool] = {var : (val == "1") for var, val in map(lambda line: line.split(': '), first_input_section)}
deps: dict[str, tuple[str, str, str]] = {res : (lhs, op, rhs)
                                         for lhs, op, rhs, _, res in map(lambda line : line.strip().split(), sys.stdin.readlines())}

# Map operation to operator
OP_MAP: dict[str, str] = {"OR" : operator.or_, "AND" : operator.and_, "XOR" : operator.xor}

@cache
def get_value(key: str) -> bool:
    # Return directly if it is an input bit
    if key in input_bits: return input_bits[key]

    # Get the value by computing the parent values recursively
    lhs, op, rhs = deps[key]
    return OP_MAP[op](get_value(lhs), get_value(rhs))

# Get answer bits by computing 2^value(zXX) for each key zXX
print(reduce(
    lambda lhs, rhs : lhs | (get_value(rhs) << int(rhs.removeprefix('z'))),
    filter(lambda z : z.startswith('z'), deps.keys()),
    0))
