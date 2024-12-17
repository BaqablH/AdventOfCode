# Read registers
registers = list(int(input().split()[-1].strip()) for _ in range(3))

# Read empty line
input()

# Read instructions
build_instructions = lambda lst : list(zip(lst[0::2], lst[1::2]))
program = build_instructions(list(map(int, input().split(": ")[1].split(','))))

# Global vars
instruction_ptr = 0
answer = []

# Run program. Used to check the output (based on sample.txt) is the same as sol1.py
A, B, C = registers
while A > 0:
    C = A >> ((A&7) ^ 5)
    B = ((A&7) ^ 3) ^ (A >> ((A&7) ^ 5))
    A >>= 3
    answer.append(B&7)

# Print answer
print(*answer, sep=',')