#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_report(case):
    with open(f'day3/{case}') as f:
        report = f.read().splitlines()
    return report


# Part 1

def check_consumption(report):
    n = len(report) # rows
    m = len(report[0]) # cols
    count = [0]*m

    for word in report:
        for i, b in enumerate(word):
            count[i] += int(b)

    gamma = ''.join(['1' if c > n/2 else '0' for c in count])
    epsilon = ''.join(['0' if c > n/2 else '1' for c in count]) # epsilon = ~gamma
    return int(epsilon, 2) * int(gamma, 2)


print('Part 1. Testing...', end=' ')
report = read_report('test')
chk = check_consumption(report)
print('Done!')
print(f'Consumption: {chk}')


print('Part 1.', end=' ')
report = read_report('input')
chk = check_consumption(report)
print('Done!')
print(f'Consumption: {chk}')
