#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Part 1
def read_signals(case):
    # For part 1 I only need the output values
    with open(f'day8/{case}') as f:
        values = [line.split(' | ')[1].split(' ') for line in f.read().splitlines()]
    return values


output_values = read_signals('input')
print(output_values)

unique_digit_segments = {2,3,4,7}

print(sum([len(word) in unique_digit_segments for entry in output_values for word in entry]))

    
