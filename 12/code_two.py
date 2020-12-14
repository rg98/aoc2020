#!/usr/bin/env python3.9
import copy

# status (E/W, N/S, Direction(N-0,E-90,S-180,W-270))
status = [0, 0]
waypoint = [10, 1]

# Read instructions
with open('in.txt', 'r') as fd:
    for step in fd:
        arg = int(step[1:-1])
        if step[0] == 'F':
            status[0] += waypoint[0] * arg
            status[1] += waypoint[1] * arg
        elif step[0] == 'N':
                waypoint[1] += arg
        elif step[0] == 'S':
                waypoint[1] -= arg
        elif step[0] == 'E':
                waypoint[0] += arg
        elif step[0] == 'W':
                waypoint[0] -= arg
        elif step[0] == 'L':
                if arg == 90:
                    _help = waypoint[0]
                    waypoint[0] = -waypoint[1]
                    waypoint[1] = _help
                elif arg == 180:
                    waypoint[0] = -waypoint[0]
                    waypoint[1] = -waypoint[1]
                elif arg == 270:
                    _help = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = -_help
        elif step[0] == 'R':
                if arg == 90:
                    _help = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = -_help
                elif arg == 180:
                    waypoint[0] = -waypoint[0]
                    waypoint[1] = -waypoint[1]
                elif arg == 270:
                    _help = waypoint[0]
                    waypoint[0] = -waypoint[1]
                    waypoint[1] = _help
        else:
            raise RuntimeError(f"Unknown command {step[0]}")
        print(step[:-1], status, waypoint)

print(f"status: {status}")
print(f"result: {abs(status[0]) + abs(status[1])}")
