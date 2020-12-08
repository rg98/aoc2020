#!/usr/bin/env python3.9
  
def check(program):
    pc = 0
    acc = 0
    check = [False] * len(program)
    while True:
        if program[pc][0] == 'n':
            if check[pc]:
                return acc
            check[pc] = True
            pc += 1
        elif program[pc][0] == 'a':
            if check[pc]:
                return acc
            check[pc] = True
            acc += program[pc][1]
            pc += 1
        elif program[pc][0] == 'j':
            if check[pc]:
                return acc
            check[pc] = True
            pc += program[pc][1]
        else:
            raise RuntimeError("Unknown opcode")

# Read program
program = []
with open('in.txt', 'r') as fd:
    for line in fd:
        if line.startswith('nop'):
            program.append(('n', 0))
        elif line.startswith('acc'):
            program.append(('a', int(line.split(' ')[1])))
        elif line.startswith('jmp'):
            program.append(('j', int(line.split(' ')[1])))
        else:
            raise RuntimeError(f"Unknown instruction: {line[:-1]}!")

# run program
print(f"accumulator: {check(program)}")

