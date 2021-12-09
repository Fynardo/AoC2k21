#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_basin(case):
    with open(f'day9/{case}', 'r') as f:
        floor = [[int(x) for x in line] for line in f.read().splitlines()]
    return floor


directions = ['N', 'E', 'S', 'W']

def peek(floor, i, j, d):
    d_builder = {'N': [-1,0], 'E':[0,1], 'S':[1,0], 'W':[0,-1]}
    x,y = d_builder[d]
    return floor[i+x][j+y]


def is_lower(floor, i, j):
    lower = True
    for d in directions:
        try:
            lower &= floor[i][j] < peek(floor, i, j, d)            
        except IndexError:
            lower &= True

    return lower


# Part 1

def find_lowers(case):
    risk_level = 0
    lower_points = []
    floor = read_basin(case)
    for i, row in enumerate(floor):
        for j, col in enumerate(row):
            if is_lower(floor, i, j):
                risk_level += col + 1
                lower_points.append((i,j))
    return lower_points, risk_level


print('Part 1. Testing...', end=' ')
assert find_lowers('test')[1] == 15
print('Done!')


print('Part 1.', end=' ')
lowers, risk_level = find_lowers('input')
print('Done!')
print(f'Evaluated Risk Level: {risk_level}')

