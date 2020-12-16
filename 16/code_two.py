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
            if (t_id >= rule[0][0] and t_id <= rule[0][1]) or (t_id >= rule[1][0] and t_id <= rule[1][1]):
                rules_cnt -= 1
        if rules_cnt == n_rules:
            invalid.append(t_id)
    return invalid

def check_tickets(rule, ticket_ids):
    """Check ticket ids: rules have the structure {'name': [[from, to], [from, to]], ...}.
       Ticket Ids have the structure [n1, n2, n3, ...]
       every ticket_id is tested for rule. If all tickets fulfill the rule return True."""
    for t_id in ticket_ids:
        if (t_id < rule[0][0] or t_id > rule[0][1]) and (t_id < rule[1][0] or t_id > rule[1][1]):
            return False
    return True

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

invalid_tickets = []
for i, ticket in enumerate(nearby_tickets):
    inv = check_rules(rules, ticket)
    if len(inv) > 0:
        invalid_tickets.append(i)
for t in reversed(invalid_tickets):
    del nearby_tickets[t]

n_rules = len(rules)
rules_single_fit = dict(map(lambda x: (x[0], -1), rules.items()))

while len(list(filter(lambda x: x == -1, rules_single_fit.values()))) > 1:
    for t_id in range(n_rules):
        ticket_ids = []
        for i in range(len(nearby_tickets)):
            ticket_ids.append(nearby_tickets[i][t_id])
        fit_rules = 0
        fitting_name = None
        fitting_id = None
        for name, rule in rules.items():
            if rules_single_fit[name] >= 0:
                continue
            if check_tickets(rule, ticket_ids):
                fit_rules += 1
                fitting_name = name
                fitting_id = t_id
        if fit_rules == 1:
            rules_single_fit[fitting_name] = fitting_id
            continue

departure_prod = 1
for name, idx in rules_single_fit.items():
    if name.startswith('departure'):
        departure_prod *= my_ticket[idx]

print(f"result: {departure_prod}")
