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


def extract_star_gears(line: str) -> list[str]:
    return re.findall(r'[*]+', line)


def extract_all_numbers(lines: list[str]) -> list[list[str]]:
    numbers_dict = {}
    for r in range(1,len(lines)-1):
        numbers_in_line = re.findall(r'\d+', lines[r])
        search_start = 0
        numbers = []
        for i in numbers_in_line:
            num_loc = lines[r].find(i, search_start)
            numbers.append((i, num_loc))
            search_start = num_loc+len(i)
        numbers_dict[r] = numbers
    return numbers_dict


def adjacent_numbers(i, numbers):
    nums = []
    for n in numbers:
        if i-1 <= n[1] <= i+1 or i-1 <= (n[1]+len(n[0])-1) <= i+1:
            nums.append(int(n[0]))
    return nums


def part2(schematic: str):
    gear_ratios_sum = 0
    with open(schematic, 'r') as file:
        lines = file.readlines()
    col_nr, row_nr = len(lines[0])+2, len(lines)+2
    lines = ['.'*col_nr] + [line.rstrip() for line in lines] + ['.'*col_nr]
    numbers = extract_all_numbers(lines)
    for r in range(1, row_nr-1):
        search_start = 0
        for i in range(lines[r].count('*')):
            gear_loc = lines[r].find('*', search_start)
            search_start = gear_loc+1
            ad_nums = adjacent_numbers(gear_loc, numbers[r-1]+numbers[r]+numbers[r+1])
            if len(ad_nums) == 2:
                gear_ratios_sum += ad_nums[0]*ad_nums[1]
    print('Gear ratios sum:', gear_ratios_sum) 


if __name__ == '__main__':
    # part1('Day3/input.txt')
    part2('Day3/input.txt')