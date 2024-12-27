def solve(dp, n): return sum(dp) if n == 0 else solve([dp[i + 1] + (dp[0] if i == 6 else 0) for i in range(8)] + [dp[0]], n - 1)
print([solve([sum(x == i for x in list(map(int, open('../inputs/06.inp').read().rstrip().split(',')))) for i in range(9)], rep) for rep in [80, 256]])
