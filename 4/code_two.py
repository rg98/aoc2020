#!/usr/bin/env python3.9
import re

def check_passport(passport):
    necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional = ['cid']
    # split passport into fields
    fields = dict(map(lambda x: x.split(':'), passport.split(' ')[1:]))
    re_byr = re.compile('\d{4}')
    re_iyr = re.compile('\d{4}')
    re_eyr = re.compile('\d{4}')
    re_hgt = re.compile('\d{2,3}(cm|in)')
    re_hcl = re.compile('#[0-9a-f]{6}')
    re_ecl = re.compile('(amb|blu|brn|gry|grn|hzl|oth)')
    re_pid = re.compile('^\d{9}$')
    if 'byr' not  in fields.keys():
        # print(f'passport: {passport} is invalid - byr is missing')
        return 0
    m_byr = re_byr.match(fields['byr'])
    if m_byr == None or 1920 > int(m_byr.group(0)) or int(m_byr.group(0)) > 2002:
        # print(f'passport: {passport} is invalid - byr is invalid or out of range')
        return 0
    if 'iyr' not  in fields.keys():
        # print(f'passport: {passport} is invalid - iyr is missing')
        return 0
    m_iyr = re_iyr.match(fields['iyr'])
    if m_iyr == None or 2010 > int(m_iyr.group(0)) or int(m_iyr.group(0)) > 2020:
        # print(f'passport: {passport} is invalid - iyr is invalid or out of range')
        return 0
    if 'eyr' not  in fields.keys():
        # print(f'passport: {passport} is invalid - eyr is missing')
        return 0
    m_eyr = re_eyr.match(fields['eyr'])
    if m_eyr == None or 2020 > int(m_eyr.group(0)) or int(m_eyr.group(0)) > 2030:
        # print(f'passport: {passport} is invalid - eyr is invalid or out of range')
        return 0
    if 'hgt' not  in fields.keys():
        # print(f'passport: {passport} is invalid - hgt is missing')
        return 0
    m_hgt = re_hgt.match(fields['hgt'])
    if m_hgt == None:
        # print(f'passport: {passport} is invalid - hgt is invalid')
        return 0
    elif m_hgt.group(1) == 'cm':
        if (150 > int(m_hgt.group(0)[:-2]) or int(m_hgt.group(0)[:-2]) > 193):
            # print(f'passport: {passport} is invalid - hgt is out of cm range')
            return 0
    elif m_hgt.group(1) == 'in':
        if (59 > int(m_hgt.group(0)[:-2]) or int(m_hgt.group(0)[:-2]) > 76):
            # print(f'passport: {passport} is invalid - hgt is out of in range')
            return 0
    else:
        # print(f'passport: {passport} is invalid - hgt has invalid unit {m_hgt.group(1)}')
        return 0
    if 'hcl' not  in fields.keys():
        # print(f'passport: {passport} is invalid - hcl is missing')
        return 0
    m_hcl = re_hcl.match(fields['hcl'])
    if m_hcl == None:
        # print(f'passport: {passport} is invalid - hcl is invalid')
        return 0
    if 'ecl' not  in fields.keys():
        # print(f'passport: {passport} is invalid - ecl is missing')
        return 0
    m_ecl = re_ecl.match(fields['ecl'])
    if 'pid' not  in fields.keys():
        # print(f'passport: {passport} is invalid - pid is missing')
        return 0
    m_pid = re_pid.match(fields['pid'])
    if m_ecl == None:
        return 0
    if m_pid == None:
        return 0
    print('passort ', end='')
    if 'cid' in fields.keys():
        del fields['cid']
    for key, value in sorted(fields.items(), key=lambda x: x[0]):
        if key == 'hgt':
            print(f'{key} : {value:5s}, ', end='')
        else:
            print(f'{key} : {value}, ', end='')
    print('is valid!')
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
    count += check_passport(passport)

print(f'Checked {count} valid passports.')
