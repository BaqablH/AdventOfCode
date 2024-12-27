import numpy as np

lines = list(open('../inputs/04.inp'))
perm = list(map(int, lines[0].rstrip().split(',')))
bingos = [np.array([np.array([int(x) for x in line.rstrip().split()]) 
            for line in lines[i:i+5]]) for i in range(2, len(lines), 6)]

# Superbingo: 10 rows, the 5 bingo rows + the 5 bingo columns
def solve(superbingo, n_round = 0):
    # Superbingo after next number is drawn
    superbingo = np.array([np.array([
            None if perm[n_round] == x else x for x in line]) for line in superbingo])

    # If any row is full of Nones, return the answer
    if any(all(map(lambda x : x is None, line)) for line in superbingo):
        return (n_round, perm[n_round] * sum(filter(None.__ne__, superbingo.flatten()))//2)

    # Try to solve for the next round
    return solve(superbingo, n_round + 1)

sols = sorted(map(lambda bingo : solve(np.concatenate([bingo, bingo.transpose()])), bingos))
print(sols[0][1])
print(sols[-1][1])