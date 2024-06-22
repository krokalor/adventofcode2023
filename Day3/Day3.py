"""
@author Karol K
"""

import re

def extract_numbers(line):
    return re.findall(r'\d+', line)

def extraxt_neighbours(number, num_loc, lines):
    previous_row = lines[0][num_loc-1:num_loc+len(number)+1]
    current_row = lines[1][num_loc-1] + lines[1][num_loc+len(number)]
    next_row = lines[2][num_loc-1:num_loc+len(number)+1]
    return previous_row+current_row+next_row

def is_next_to_gear(neighbours):
    return bool(re.search(r'[^0-9.]+',neighbours))

def part1(schematic):
    gear_ratios_sum = 0
    with open(schematic, 'r') as file:
        lines = file.readlines()
    col_nr, row_nr = len(lines[0])+2, len(lines)+2
    lines = ['.'*col_nr] + ['.' + line.rstrip() + '.' for line in lines] + ['.'*col_nr]
    for r in range(1, row_nr-1):
        nums = extract_numbers(lines[r])
        search_start = 0
        for i in nums:
            num_loc = lines[r].find(i, search_start)
            neighbours = extraxt_neighbours(i, num_loc, lines[r-1:r+2])
            gear_ratios_sum += int(i) if is_next_to_gear(neighbours) else 0
            print(i, neighbours, is_next_to_gear(neighbours))
            search_start = num_loc+len(i)
    print('Gear ratios sum:', gear_ratios_sum)

if __name__ == '__main__':
    part1('Day3/input.txt')