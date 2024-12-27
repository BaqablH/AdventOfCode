from sol1 import *

def test(f, args, exp):
    ans = f(*args if isinstance(args, tuple) else args)
    if (ans == exp): print(f"Case {args}: OK")
    else: print(f"Case {args}: FAILED. Expected {exp}, got {ans}")

test(mix_and_prune, (42, 15), 37)
test(mix_and_prune, (100000000, 0), 16113920)
test(next_secret, (123, ), 15887950)
