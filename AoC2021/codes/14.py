from collections import Counter
from functools import reduce

lines = open('../inputs/14.inp').read().splitlines()
instrs = {(l[0], l[1]) : l[-1] for l in lines[2:]}

# Updates counter of pairs from one step to the next
update = lambda ctr, _ : sum((Counter({(P[0], instrs[P]) : k}) + Counter({(instrs[P], P[1]) : k}) for P, k in ctr.items()), Counter())

# Returns counter of pairs of consecutive elements after n steps
final_ctr = lambda n : reduce(update, range(n), Counter(zip(lines[0], lines[0][1:]))).items()

# Returns max difference given by a Counter.most_common()
maxdiff = lambda com : com[0][1] - com[-1][1]

# Computes number of appearances of each character from Counter of pairs
char_counter = lambda ctr : sum((Counter({P[0] : k}) for P, k in ctr), Counter({lines[0][-1] : 1}))

# Solves the problem for n steps
solve = lambda n : maxdiff(char_counter(final_ctr(n)).most_common())

print(solve(10), solve(40), sep = '\n')

