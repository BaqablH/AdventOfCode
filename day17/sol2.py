from itertools import product

# Read registers
registers = list(int(input().split()[-1].strip()) for _ in range(3))

# Read empty line
input()

# Get program (in binary)
binary_program = list(map(int, "".join(
    bin(8 | int(x)).removeprefix('0b1')[::-1] for x in input().split(": ")[1].split(','))))

# Array of the bits of candidate initial register A (with extra padding)
A = [None]*len(binary_program) + [0]*9

answer = None
def backtrack(i = 15):
    global answer

    # No need to look further
    if answer is not None:
        return
    
    # Answer found
    if i == -1:
        answer = sum(x << i for i, x in enumerate(A))
        return 
    
    # Iterate over the possible 8 next triplets of bits, ordered by most significant bit
    for c, b, a in product([0, 1], repeat=3):
        # Set A for the new elements
        for j, x in enumerate([a, b, c]):
            A[3*i + j] = x

        # Get shift part in our equation and set conditions
        shift = ((c^1) << 2) ^ (b << 1) ^ (a^1)
        kth_condition_satisfied = lambda k : binary_program[k] == A[k] ^ int(k%3 != 2) ^ A[k + shift]

        # If all bits satisfy the bit equation, set the specific A bits and continue the backtracking
        if all(kth_condition_satisfied(3*i + j) for j in range(3)):
            backtrack(i - 1)

# Start backtracking
backtrack()

# Print answer
print(answer)
