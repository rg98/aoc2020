#!/usr/bin/env python3.9
import copy
  
def check(program):
    pc = 0
    acc = 0
    check = [False] * len(program)
    while pc < len(program):
        if program[pc][0] == 'n':
            if check[pc]:
                return False, acc
            check[pc] = True
            pc += 1
        elif program[pc][0] == 'a':
            if check[pc]:
                return False, acc
            check[pc] = True
            acc += program[pc][1]
            pc += 1
        elif program[pc][0] == 'j':
            if check[pc]:
                return False, acc
            check[pc] = True
            if pc + program[pc][1] > len(program) or pc + program[pc][1] < 0:
                return False, acc
            pc += program[pc][1]
        else:
            raise RuntimeError("Unknown opcode")
    return True, acc

# Read program
program = []
with open('in.txt', 'r') as fd:
    for line in fd:
        if line.startswith('nop'):
            program.append(('n', int(line.split(' ')[1])))
        elif line.startswith('acc'):
            program.append(('a', int(line.split(' ')[1])))
        elif line.startswith('jmp'):
            program.append(('j', int(line.split(' ')[1])))
        else:
            raise RuntimeError(f"Unknown instruction: {line[:-1]}!")

# run program
for i in range(len(program)):
    if program[i][0] == 'n':
        test_program = copy.deepcopy(program)
        test_program[i] = ('j', test_program[i][1])
    elif program[i][0] == 'j':
        test_program = copy.deepcopy(program)
        test_program[i] = ('n', test_program[i][1])
    else:
        continue
    succ, acc = check(test_program)
    if succ:
        print(f"accumulator: {acc}")

