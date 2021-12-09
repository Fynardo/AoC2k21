#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_basin(case):
    with open(f'day9/{case}', 'r') as f:
        floor = [[int(x) for x in line] for line in f.read().splitlines()]
    return floor


def is_lower(floor, i, j, d):
    try:
        if d == 'N':
            return floor[i][j] < floor[i-1][j]
        elif d == 'E':
            return floor[i][j] < floor[i][j+1]
        elif d == 'S':
            return floor[i][j] < floor[i+1][j]
        elif d == 'W':
            return floor[i][j] < floor[i][j-1]
    except IndexError:
       return True 


# Part 1
directions = ['N', 'E', 'S', 'W']

def find_lowers(case):
    retval = 0
    floor = read_basin(case)
    for i, row in enumerate(floor):
        for j, col in enumerate(row):
            if all([is_lower(floor, i, j, d) for d in directions]):
                retval += col + 1
    return retval


print('Part 1. Testing...', end=' ')
assert find_lowers('test') == 15
print('Done!')


print('Part 1.', end=' ')
lowers = find_lowers('input')
print('Done!')
print(f'Evaluated Risk Level: {lowers}')

