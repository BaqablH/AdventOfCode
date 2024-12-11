import functools

MAX_BLINKS: int = 25

@functools.cache
def count(x: int, blinks: int = 0) -> int:
    if blinks == MAX_BLINKS:
        return 1
    if len(str(x)) % 2 == 0:
        return sum(count(int(half), blinks + 1) for half in [str(x)[:len(str(x))//2], str(x)[len(str(x))//2:]])
    return count(max(1, 2024*int(x)), blinks + 1)

print(sum(map(lambda x : count(int(x)), input().split())))
