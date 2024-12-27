def solve(line, stack="", x=0):
    # If we have read the entire line, convert to base 5
    if x == len(line):
        return (0, int(stack[::-1].translate(str.maketrans("([{<", "1234")), 5))
    # If character is opening, append it to the stack
    if line[x] in '([{<':
        return solve(line, stack + line[x], x + 1)
    # If character is closing and good, pop it from the stack
    if stack and abs(ord(line[x]) - ord(stack[-1])) <= 2:
        return solve(line, stack[:-1], x + 1)
    # Return penalty
    return ({')': 3, ']': 57, '}': 1197, '>': 25137}[line[x]], 0)

middle_element = lambda v : v[len(v)//2]
sols = list(map(solve, open('../inputs/10.inp').read().splitlines()))

print(sum(s[0] for s in sols))
print(middle_element(sorted(b for _, b in sols if b > 0)))
