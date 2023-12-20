"""
@author Karol K
@date 14/12/2023
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


class Day9:
    __input = 'input.txt'

    @staticmethod
    def part1(test=True):
        """9.1"""
        print('AoC23: 8.1\n')
        Day9.__input = 'test.txt' if test else Day9.__input
        with open(Day9.__input, 'r') as file:
            lines = file.readlines()
        history = []
        for line in lines:
            history.append([int(i) for i in line.split()])
        print(history)


if __name__ == '__main__':
    Day9.part1()
