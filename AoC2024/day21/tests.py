from sol1 import *

def test(input, exp):
    ans = compute(*input)
    if (ans == exp): print(f"Case {input}: OK")
    else : print(f"Case {input}: expected {exp}, got {ans}")

test(('A', 'v', 2), 3)
test(('v', '<', 2), 2)
test(('<', '<', 2), 1)
test(('<', 'A', 2), 4)

test(('A', '>', 2), 2)
test(('>', '>', 2), 1)
test(('>', '^', 2), 3)
test(('^', 'A', 2), 2)

test(('A', '<', 1), 10)
test(('<', 'A', 1), 8)
