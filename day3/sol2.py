import re, sys

def process(text, do: bool = True):
    match = re.search(r"do\(\)|don't\(\)", text)
    next_do, index = (match.group() == "do()", match.start()) if match else (False, len(text))
    return (sum(int(x)*int(y) for x, y in re.findall(r"mul\((\d+),\s*(\d+)\)", text[:index])) if do else 0) + \
            (0 if index == len(text) else process(text[index+4:], next_do))

print(process(sys.stdin.read()))