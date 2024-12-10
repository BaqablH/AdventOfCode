import itertools
from typing import List, Union, Iterable, Tuple, Callable, Generator

# Build chain from input
chain : List[Union[str, int]] = \
    [i//2 if i&1 == 0 else '.' for i, c in enumerate(input()) for _ in range(int(c))]

# Reversed iterator on the chain, enumerated
rev_iter: Iterable[Tuple[int, int]] = iter((i, val) for i, val in list(enumerate(chain))[::-1] if val != '.')

# Get next relevant number in the chain. If the current position has an integer, return it,
# Otherwise return the next integer as seen from the end
get_next: Callable[[int, int], Tuple[int, int]] = lambda j, val : (j, val) if isinstance(val, int) else next(rev_iter)

# Generate the numbers of the final chain, multiplied by its index
def iterations() -> Generator[int, None, None]:
    j: int = len(chain)
    for i, val in itertools.takewhile(lambda P: P[0] < j, enumerate(chain)):
        j, val2 = get_next(j, val)
        yield i*val2

print(sum(iterations()))