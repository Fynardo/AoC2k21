#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Day 1. Global Stuff
def scan(case):
    with open(f'day1/{case}', 'r') as f:
        depths = [int(x) for x in f.read().splitlines()]
    return depths


def measure(data, i, w):
    """
    Read the sliding window from the sonar data and return its sum
    param: data. The sonar data (list of ints)
    param: i. The index of the pointer
    param: w. The size of the window
    return: The measure
    """
    return sum(data[i:(i+w)])


def evaluate(depths, w, offset):
    """
    Counts how manty times a depth measure increases from previous one.
    param: depths. Sonar data (list of ints)
    param: w. Size of the window
    param: offset: The separation between one measure and the next
    return: number of increasing measures
    """
    n = len(depths)
    larger = sum([measure(depths, i, w) < measure(depths, i + offset, w) for i in range(n - w)])
    return larger


# Part 1
print('Part 1. Testing...', end=' ')
depths = scan('test')
assert evaluate(depths, 1, 1) == 7
print('Done!')


print('Part 1...', end=' ')
depths = scan('input')
ev = evaluate(depths, 1, 1)
print(f'Done!')
print(f'Found {ev} increasing measurements.')


# Part 2
print('Part 2. Testing...', end=' ')
depths = scan('test')
assert evaluate(depths, 3, 1) == 5 

print('Part 2...', end=' ')
depths = scan('input')
ev = evaluate(depths, 3, 1)
print(f'Done!')
print(f'Found {ev} increasing measurements.')

