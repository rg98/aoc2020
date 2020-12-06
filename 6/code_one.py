#!/usr/bin/env python3.9

def count_questions(group):
    questions = {}
    for c in group:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            if c in questions.keys():
                questions[c] += 1
            else:
                questions[c] = 1
    return len(questions)

groups = ['']
with open('in.txt', 'r') as fd:
    for line in fd:
        if len(line) > 1:
            groups[-1] += line[:-1]
        else:
            groups.append('')

count = 0
for group in groups:
    count += count_questions(group)

print(f'Sum of all groups: {count}.')
