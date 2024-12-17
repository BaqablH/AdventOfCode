# Read registers
registers = list(int(input().split()[-1].strip()) for _ in range(3))

# Read empty line
input()

# Read instructions
build_instructions = lambda lst : list(zip(lst[0::2], lst[1::2]))
program = build_instructions(list(map(int, input().split(": ")[1].split(','))))

# Get combo
combo = lambda n : n if n < 4 else registers[n & 3]

# Global vars
instruction_ptr = 0
answer = []

# Instructions
def adv(op: int): registers[0] >>= combo(op)
def bxl(op: int): registers[1] ^= op
def bst(op: int): registers[1] = combo(op) & 7
def jnz(op: int): global instruction_ptr; instruction_ptr = op if registers[0] > 0 else instruction_ptr
def bxc(op: int): registers[1] ^= registers[2]
def out(op: int): answer.append(combo(op) & 7)
def bdv(op: int): registers[1] = registers[0] >> combo(op)
def cdv(op: int): registers[2] = registers[0] >> combo(op)

# (Indexed) list of instructions
instr = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

# Run program
while instruction_ptr < len(program):
    ins, op = program[instruction_ptr]
    instruction_ptr += 1
    instr[ins](op)

# Print answer
print(*answer, sep=',')