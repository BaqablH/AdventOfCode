N, M = 7, 5

def generate_masks():
    while True:
        # Read description. Leading char indicates whether it's a lock ('#') or key ('.'), and build the bitmask
        leading_char: str = input()[0]
        get_mask = lambda desc: sum(((x == leading_char) << i*M + j for i, row in enumerate(desc) for j, x in enumerate(row)))
        yield (leading_char, get_mask([input() for _ in range(N - 1)]))

        # Read empty line. If it fails, it means input is over
        try: input()
        except: return

# Store masks and filter by type. Then print how many pairs (key, lock) lock bitmask included in the key bitmask
mask_pairs: list[tuple[str, int]] = list(generate_masks())
get_mask_by_char = lambda c : (mask for leading_char, mask in mask_pairs if leading_char == c)

print(sum((lock & key) == lock for lock in get_mask_by_char('#') for key in get_mask_by_char('.')))