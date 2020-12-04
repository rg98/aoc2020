#!/usr/bin/env python3.9

def check_passport(passport, necessary, optional):
    # split passport into fields
    fields = dict(map(lambda x: x.split(':'), passport.split(' ')[1:]))
    for check in necessary:
        if check not in fields.keys():
            return 0
    return 1

passports = ['']
with open('in.txt', 'r') as fd:
    for line in fd:
        if len(line) > 1:
            passports[-1] += ' ' + line[:-1]
        else:
            passports.append('')

count = 0
for passport in passports:
    count += check_passport(passport, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cid'])

print(f'Checked {count} valid passports.')
print(f'{len(passports)} checked!')
