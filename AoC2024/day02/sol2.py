import sys

check_seq_is_increasing = lambda lst: all(1 <= r - l <= 3 for (l, r) in zip(lst, lst[1:]))
find_next_fail_pos = lambda lst: \
    next((i for (i, (l, r)) in enumerate(zip(lst, lst[1:])) if not(1 <= r - l <= 3)), None)
check_seq_is_almost_increasing_from_failed_index = lambda lst, ind: \
    ind is None or any(find_next_fail_pos(lst[:ind+offset] + lst[ind+offset+1:]) is None for offset in [0, 1])
check_seq_is_almost_increasing = lambda lst : check_seq_is_almost_increasing_from_failed_index(
                                                            lst, find_next_fail_pos(lst))

read_line = lambda line : list(map(int, line.split()))
print(sum(check_seq_is_almost_increasing(line) or check_seq_is_almost_increasing(line[::-1])
            for line in map(read_line, sys.stdin)))