import sys

read_line = lambda line : list(map(int, line.split()))
check_increasing = lambda L, R: all(1 <= r - l <= 3 for (l, r) in zip(L, R))
is_safe = lambda L, R: check_increasing(L, R) or check_increasing(R, L)
print(sum(is_safe(line, line[1:]) for line in map(read_line, sys.stdin)))