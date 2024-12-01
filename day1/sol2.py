import sys
import re
from operator import itemgetter
from collections import Counter

# Regex to match two integers with optional whitespace
read_line = lambda line : tuple(map(int, re.search(r'\s*(\d+)\s+(\d+)\s*', line).groups()))
input = list(map(read_line, sys.stdin))
r_counter = Counter(map(itemgetter(1), input))
print(sum(x * r_counter[x] for x in map(itemgetter(0), input)))