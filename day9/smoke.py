#!/usr/bin/env python
# -*- coding: utf-8 -*-


import functools


def read_basin(case):
    with open(f'day9/{case}', 'r') as f:
        floor = [[int(x) for x in line] for line in f.read().splitlines()]
    return floor


directions = ['N', 'E', 'S', 'W']
d_builder = {'N': [-1,0], 'E':[0,1], 'S':[1,0], 'W':[0,-1]}

def plan_route(i, j, d):
    x, y = d_builder[d]
    if i+x < 0 or j+y < 0:
        raise IndexError
    else:
        return i+x, j+y
    

def peek(floor, i, j, d):
    x,y = plan_route(i,j,d)
    return floor[x][y]


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


# Part 2
def flows_upwards(floor, i, j, d):
    try:
        p = peek(floor, i, j, d)
        if p < 9 and p > floor[i][j]:
            return True
        else:
            return False
    except IndexError:
        return False


def locate_basins(case):
    floor = read_basin(case)
    basins = []
    lowers, _ = find_lowers(case)

    for l in lowers:
        explored = set()
        basin_elements = set()
        frontier = [l]

        while frontier:
            i, j = frontier.pop(0)
            if (i,j) not in explored:
                explored.add((i,j))
                for d in directions:
                    if flows_upwards(floor, i, j, d):
                        if (i, j) not in basin_elements:
                            basin_elements.add((i, j))
                        frontier.insert(0, plan_route(i, j, d))
                        if plan_route(i, j, d) not in basin_elements:
                            basin_elements.add(plan_route(i, j, d))
        basins.append(len(basin_elements))
    return basins


print('Part 2. Testing...', end=' ')
basins = locate_basins('test')
assert functools.reduce(lambda x,y: x * y, sorted(basins, reverse=True)[:3]) == 1134
print('Done!')


print('Part 2.', end=' ')
basins = locate_basins('input')
total = functools.reduce(lambda x,y: x * y, sorted(basins, reverse=True)[:3])
print('Done!')
print(f'Located basins, multiplied size: {total}')

