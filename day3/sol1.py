import re, sys

print(sum(int(x)*int(y) for x, y in re.findall(r"mul\((\d+),\s*(\d+)\)", sys.stdin.read())))