#!/usr/bin/env python3.9
import copy

# rules
rules = {}

my_ticket = []

nearby_tickets = []

def check_rules(rules, ticket):
    """Check rules: rules have the structure {'name': [[from, to], [from, to]], ...}.
       Tickets have the structure [n1, n2, n3, ...]
       every rule is tested for every number. The returned array contains all
       numbers not fulfilling any rule."""
    n_rules = len(rules) * 2
    invalid = []
    for t_id in ticket:
        rules_cnt = n_rules
        for name, rule in rules.items():
            if t_id >= rule[0][0] and t_id <= rule[0][1]:
                rules_cnt -= 1
            if t_id >= rule[1][0] and t_id <= rule[1][1]:
                rules_cnt -= 1
        if rules_cnt == n_rules:
            invalid.append(t_id)
    return invalid

# Read rules
with open('in.txt', 'r') as fd:
    for rule in fd:
        if len(rule) == 1:
            break
        name, ranges = rule[:-1].split(': ')
        r1, r2 = ranges.split(" or ")
        r1_from, r1_to = r1.split("-")
        r2_from, r2_to = r2.split("-")
        rules[name] = [[int(r1_from), int(r1_to)], [int(r2_from), int(r2_to)]]

    for ticket in fd:
        if len(ticket) == 1:
            break
        if ticket.startswith('your '):
            continue
        my_ticket = list(map(lambda x: int(x), ticket[:-1].split(',')))

    for ticket in fd:
        if ticket.startswith('nearby '):
            continue
        nearby_tickets.append(list(map(lambda x: int(x), ticket[:-1].split(','))))

invalids = []
invalid_tickets = []
for i, ticket in enumerate(nearby_tickets):
    inv = check_rules(rules, ticket)
    if len(inv) > 0:
        invalids.extend(inv)
        invalid_tickets.append(i)

tser = sum(invalids)

print(f"result: {tser}, {invalid_tickets}")
