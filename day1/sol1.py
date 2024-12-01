import sys
import re
from operator import itemgetter

# Regex to match two integers with optional whitespace
read_line = lambda line : tuple(map(int, re.search(r'\s*(\d+)\s+(\d+)\s*', line).groups()))
input = list(map(read_line, sys.stdin))
sorted_by_nth = lambda n : sorted(map(itemgetter(n), input))
print(sum(abs(x - y) for x, y in zip(sorted_by_nth(0), sorted_by_nth(1))))