#!/usr/bin/env python
# -*- coding: utf-8 -*-


def scan_crabs(case):
    with open(f'day7/{case}') as f:
        crabs = [int(x) for x in f.readline().split(',')]
    return crabs


def calculate_fuel(i, crabs):
    """ Calculates fuel consumption of every crab moving to 'i' position """
    return sum([abs(crab - i) for crab in crabs])




# Part 1
def arrange_crabs(case):
    """ I suppose that the cheapest move is to go to the middle of the pack, the median. """
    crabs = scan_crabs(case)
    m = sorted(crabs)
    n = len(crabs)
    start = m[n//2]
    return calculate_fuel(start, crabs)


print('Part 1. Testing...', end=' ')
assert arrange_crabs('test') == 37
print('Done!')

print('Part 1...', end=' ')
print('Done!')
print(f'Total fuel consumption: {arrange_crabs("input")}')




