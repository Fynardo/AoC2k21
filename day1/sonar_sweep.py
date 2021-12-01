#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Part 1
print('Day 1. Part 1.')
with open('day1/input', 'r') as f:
    depths = [int(x) for x in f.read().splitlines()]

larger = sum([x < y for x, y in zip(depths[:-1], depths[1:])])
print(f'Done! {larger} increasing measurements.')

