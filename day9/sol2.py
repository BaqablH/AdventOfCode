import itertools
from typing import List, Union

# Read input
inp = [(i//2 if i&1 == 0 else '.', int(c)) for i, c in enumerate(input())]

for r_val in list(range(len(inp)//2 + 1))[::-1]:
    for ind, (rv, rr) in enumerate(inp):
        if rv == r_val:
            r_reps, rhs_ind = rr, ind
    if r_val == '.': continue
    for lhs_ind, (l_val, l_reps) in enumerate(inp):
        if lhs_ind >= rhs_ind:
            break
        if l_val != '.': continue
        if l_reps >= r_reps:
            change = True
            inp = inp[:lhs_ind] + [(r_val, r_reps), ('.', l_reps - r_reps)] + inp[lhs_ind + 1:rhs_ind] + [('.', r_reps)] + inp[rhs_ind + 1:]
            break

new_list = list(0 if val == '.' else val for i, (val, reps) in enumerate(inp) for _ in range(reps))
print(sum(i*x for i, x in enumerate(new_list)))
