import sys

read_line = lambda line : list(map(int, line.split()))
check_increasing = lambda L, R: all(1 <= r - l <= 3 for (l, r) in zip(L, R))
call_adjacent = lambda func, lst : func(lst[:-1], lst[1:])
call_adjacent2 = lambda func, lst : func(lst[1:], lst[:-1])

def check_almost_increasing(line):
    ind = next((i for (i, (l, r)) in enumerate(zip(line, line[1:])) if not(1 <= r - l <= 3)), None)
    return ind is None or call_adjacent(check_increasing, line[:ind] + line[ind+1:]) or call_adjacent(check_increasing, line[:ind + 1] + line[ind+2:])

def check_almost_decreasing(line):
    ind = next((i for (i, (l, r)) in enumerate(zip(line, line[1:])) if not(1 <= l - r <= 3)), None)
    return ind is None or call_adjacent2(check_increasing, line[:ind] + line[ind+1:]) or call_adjacent2(check_increasing, line[:ind + 1] + line[ind+2:])

is_safe = lambda line: check_almost_increasing(line) or check_almost_decreasing(line)
print(sum(is_safe(line) for line in map(read_line, sys.stdin)))