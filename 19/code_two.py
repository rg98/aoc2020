#!/usr/bin/env python3.9
import re

def apply_rule(rule, rules):
    result = ""
    if '|' in rule:
        left, right = rule.split(' | ')
        return '(' + apply_rule(left, rules) + '|' + apply_rule(right, rules) + ')'
    else:
        for s in rule.split(' '):
            # Digit
            if s == '8':
                result += '(' +  apply_rule('42', rules) + '+)'
            elif rule == rules['11']:
                result += '(' + apply_rule('42', rules) + apply_rule('31', rules) + ')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) + ')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) + ')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) + ')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) +')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) +')|(' \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('42', rules) \
                          + apply_rule('42', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) \
                          + apply_rule('31', rules) + apply_rule('31', rules) +')'
            elif s[0] in '0123456789':
                result += apply_rule(rules[s], rules)
            elif s[0] == '"':
                result += s[1]
    return result
        

rules = {}
messages = []

# Read rules
with open('in.txt', 'r') as fd:
    for rule in fd:
        if len(rule) == 1:
            break
        n, r = rule[:-1].split(':')
        rules[n] = r[1:]

    for message in fd:
        messages.append(message[:-1])

print(rules)
print(f"{len(messages)} messages")

regex = apply_rule(rules['0'], rules)

print(regex)

re_match = re.compile(regex)

valid_messages = 0
for message in messages:
    m = re_match.match(message)
    if m and m.span()[1] == len(message):
        valid_messages += 1

print(valid_messages)
