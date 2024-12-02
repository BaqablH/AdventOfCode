import sys

read_line = lambda line : list(map(int, line.split()))
check_increasing = lambda L, R: all(1 <= r - l <= 3 for (l, r) in zip(L, R))
adj_callback = lambda func, lst, ordered : \
    func(lst[:-1] if ordered else lst[1:], lst[1:] if ordered else lst[:-1])
def check_almost_monotonous(line, ordered):
    ind = next((i for (i, (l, r)) in enumerate(adj_callback(zip, line, ordered))
                    if not(1 <= r - l <= 3)), len(line))
    return any(adj_callback(check_increasing, line[:ind+offset] + line[ind+offset+1:], ordered)
                    for offset in [0, 1])
is_safe = lambda line: any(check_almost_monotonous(line, ordered) for ordered in [True, False])
print(sum(is_safe(line) for line in map(read_line, sys.stdin)))