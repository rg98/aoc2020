#!/usr/bin/env python3.9

def count_questions(group, size):
    questions = {}
    for c in group:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            if c in questions.keys():
                questions[c] += 1
            else:
                questions[c] = 1
    all_yes = list(filter(lambda x: questions[x] == size, questions.keys()))
    return len(all_yes)

groups = [('', 0)]
with open('in.txt', 'r') as fd:
    for line in fd:
        if len(line) > 1:
            groups[-1] = (groups[-1][0] + line[:-1], groups[-1][1] + 1)
        else:
            groups.append(('', 0))

count = 0
for group, size in groups:
    count += count_questions(group, size)

print(f'Sum of all groups: {count}.')
