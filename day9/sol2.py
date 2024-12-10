from typing import List, Union

# Transform each input character to its value and repetition count
inp: List[Union[int, str]] = [(i//2 if i&1 == 0 else '.', int(c)) for i, c in enumerate(input())]

# For each value in the input (for larger to smaller), try to replace in its new position, and update the list
for r_val in list(range(len(inp)//2 + 1))[::-1]:
    # Find current value index and repetition counter
    rhs_ind, r_reps = next((ind, rr) for ind, (rv, rr) in enumerate(inp) if rv == r_val)

    # Find next space for the value, None if there is none.
    # Only consider empty spaces, among them get the first with at least r_reps spaces
    lhs_ind, l_reps = next(((lhs_ind, l_reps) for lhs_ind, (_, l_reps) in
                                filter(lambda T: T[1][0] == '.', enumerate(inp[:rhs_ind])) if l_reps >= r_reps), (None, None))

    # Update the list by moving the right index to the left
    if lhs_ind is not None:
        inp = inp[:lhs_ind] + [(r_val, r_reps), ('.', l_reps - r_reps)] + inp[lhs_ind + 1:rhs_ind] + [('.', r_reps)] + inp[rhs_ind + 1:]

# Expand the summary list, and perform the final computation
print(sum(i*x for i, x in enumerate(0 if val == '.' else val for val, reps in inp for _ in range(reps))))
