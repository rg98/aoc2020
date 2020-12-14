#!/usr/bin/env python3.9
import copy

# status (E/W, N/S, Direction(N-0,E-90,S-180,W-270))
status = [0, 0, 90]

# Read instructions
with open('in.txt', 'r') as fd:
    for step in fd:
        arg = int(step[1:-1])
        if step[0] == 'F':
            if status[2] == 0:
                status[0] += arg
            elif status[2] == 90:
                status[1] -= arg
            elif status[2] == 180:
                status[0] -= arg
            elif status[2] == 270:
                status[1] += arg
            else:
                raise RuntimeError(f"Unknown direction {status[2]}")
        elif step[0] == 'N':
                status[0] += arg
        elif step[0] == 'S':
                status[0] -= arg
        elif step[0] == 'E':
                status[1] -= arg
        elif step[0] == 'W':
                status[1] += arg
        elif step[0] == 'L':
                status[2] -= arg
                if status[2] < 0:
                    status[2] += 360
                elif status[2] >= 360:
                    status[2] -= 360
        elif step[0] == 'R':
                status[2] += arg
                if status[2] < 0:
                    status[2] += 360
                elif status[2] >= 360:
                    status[2] -= 360
        else:
            raise RuntimeError(f"Unknown command {step[0]}")

print(f"status: {status}")
print(f"result: {abs(status[0]) + abs(status[1])}")
