from itertools import product

registers = list(int(input().split()[-1].strip()) for _ in range(3))

# Read empty line
input()

# Get program (in binary)
program = list(map(int, input().split(": ")[1].split(',')))
binary_program = list(map(int, bin(sum(x << (3*i) for i, x in enumerate(program))).removeprefix('0b')))
binary_program = binary_program[::-1] + [0]*(3*len(program) - len(binary_program))

# Array of the bits of candidate initial register A
A = [None]*(3 * len(program))

# Get n-th element of A. If unset, default to array Q
def get(Q, n):
    if n >= len(A): return 0
    if A[n] is None: return Q[n % 3]
    return A[n]

answer = None
def backtrack(i = 15):
    global answer

    # No need to look further
    if answer is not None:
        return
    
    # Answer found
    if i == -1:
        answer = sum(x << i for i, x in enumerate(A[::1]))
        return 
    
    # Iterate over the possible 8 next triplets of bits
    for P in product([0, 1], repeat=3):
        # Unset A on the given bits
        for j in range(3):
            A[3*i + j] = None

        # Order by most significant bit
        c, b, a = P

        # Get shift part in our equation
        shift = ((c^1) << 2) ^ (b << 1) ^ (a^1)

        # A is ordered the other way around
        Q = [a, b, c]

        # If all bits satisfy the bit equation, set the specific A bits and continue the backtracking
        if all(
            binary_program[3*i + j] == get(Q, 3*i + j) ^ int(j != 2) ^ get(Q, 3*i + j + shift) for j in range(3)
        ):
            for j in range(3):
                A[3*i + j] = Q[j]
            backtrack(i - 1)

# Start backtracking
backtrack()

# Print answer
print(answer)
