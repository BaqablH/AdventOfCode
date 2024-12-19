import sys

get_str_with_length = lambda s : (s.strip(), len(s.strip())) 

# Read patterns
patterns: list[tuple[str, int]] = list(map(get_str_with_length, sys.stdin.readline().split(',')))

# Read empty line
sys.stdin.readline()

# Count number of solutions with a DP
def has_solution(design: str, N: int):
    dp: list[int] = [1]
    for i in range(1, N + 1):
        dp.append(sum(dp[i - L] for pattern, L in patterns if i >= L and design[i - L:i] == pattern))
    return dp[N]

# Print answer
print(sum(map(lambda case : has_solution(*get_str_with_length(case)), sys.stdin.readlines())))

