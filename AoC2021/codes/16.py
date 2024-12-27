from operator import *
from functools import reduce

# Get chunk and update p
def get_chunk(s, p, k):
    return int(s[p:p+k], 2), p + k

# Parse literal packet
def parse_literal(s, p):
    val, last = 0, '1'
    while last != '0':
        last = s[p]
        x, p = get_chunk(s, p, 5)
        val = 16*val + (x & 15)
    return p, val

# Parse literal packet
def parse_packet(s, p = 0):
    # Get version and type ID
    vers, p = get_chunk(s, p, 3)
    type_id, p = get_chunk(s, p, 3)

    # Parse literal if needed
    if type_id == 4:
        return vers, *parse_literal(s, p)

    # Get length id
    length_id, p = get_chunk(s, p, 1)
    
    # Values in subpackets
    vals = []

    # Read subpacket, update sum of versions, append value to vals
    def update():
        nonlocal p, vers
        t, p, val = parse_packet(s, p)
        vers += t
        vals.append(val)

    # Parse subpackets
    if length_id == 0:
        length, p = get_chunk(s, p, 15)
        end = p + length
        while p != end:
            update()
    else:
        number, p = get_chunk(s, p, 11)
        for _ in range(number):
            update()

    # Compute value drom subpackets and return
    val = reduce([add, mul, min, max, None, gt, lt, eq][type_id], vals)
    return vers, p, val

# Convert to binary without forgetting leading zeroes
def conv(s):
    t = bin(int(s, 16))[2:]
    return '0'*(4*len(s) - len(t)) + t

suma, _, val = parse_packet(conv(open('../inputs/16.inp').read().strip()))
print(suma, val, sep='\n')
