"""
@author Karol K
@date 01/12/2023
"""

from string import whitespace

import numpy as np


class Day3:
    ''''Class containing day 3 solutions'''
    __schematic = 'input.txt'
    __symbols = '@*/+#=$%-&'

    def __init__(self):
        """Empty constructor"""

    @staticmethod
    def get_part_points(lines, nr, nc):
        valid_points_matrix = np.zeros((nr, nc))
        for i in range(nr):
            for j in range(nc):
                if lines[i][j] in Day3.__symbols:
                    pass
                    if 0 < i < nr-1 and 0 < j < nc:
                        # upper row
                        valid_points_matrix[i-1][j-1] = 1
                        valid_points_matrix[i-1][j] = 1
                        valid_points_matrix[i-1][j+1] = 1
                        # current row
                        valid_points_matrix[i][j-1] = 1
                        valid_points_matrix[i][j+1] = 1
                        # lower row
                        valid_points_matrix[i+1][j-1] = 1
                        valid_points_matrix[i+1][j] = 1
                        valid_points_matrix[i+1][j+1] = 1
                    elif i == 0 and 0 < j < nc:
                        # current row
                        valid_points_matrix[i][j-1] = 1
                        valid_points_matrix[i][j+1] = 1
                        # lower row
                        valid_points_matrix[i+1][j-1] = 1
                        valid_points_matrix[i+1][j] = 1
                        valid_points_matrix[i+1][j+1] = 1
                    elif i == nr-1 and 0 < j < nc:
                        # upper row
                        valid_points_matrix[i-1][j-1] = 1
                        valid_points_matrix[i-1][j] = 1
                        valid_points_matrix[i-1][j+1] = 1
                        # current row
                        valid_points_matrix[i][j-1] = 1
                        valid_points_matrix[i][j+1] = 1
                    elif 0 < i < nr-1 and j == 0:
                        # upper row
                        valid_points_matrix[i-1][j] = 1
                        valid_points_matrix[i-1][j+1] = 1
                        # current row
                        valid_points_matrix[i][j+1] = 1
                        # lower row
                        valid_points_matrix[i+1][j] = 1
                        valid_points_matrix[i+1][j+1] = 1
                    elif 0 < i < nr-1 and j == nc:
                        # upper row
                        valid_points_matrix[i-1][j-1] = 1
                        valid_points_matrix[i-1][j] = 1
                        # current row
                        valid_points_matrix[i][j-1] = 1
                        # lower row
                        valid_points_matrix[i+1][j-1] = 1
                        valid_points_matrix[i+1][j] = 1
                    elif i == 0 and j == 0:
                        # current row
                        valid_points_matrix[i][j+1] = 1
                        # lower row
                        valid_points_matrix[i+1][j] = 1
                        valid_points_matrix[i+1][j+1] = 1
                    elif i == 0 and j == nc-1:
                        # current row
                        valid_points_matrix[i][j-1] = 1
                        # lower row
                        valid_points_matrix[i+1][j-1] = 1
                        valid_points_matrix[i+1][j] = 1
                    elif i == nr-1 and j == 0:
                        # upper row
                        valid_points_matrix[i-1][j] = 1
                        valid_points_matrix[i-1][j+1] = 1
                        # current row
                        valid_points_matrix[i][j+1] = 1
                    elif i == nr-1 and j == nc-1:
                        # upper row
                        valid_points_matrix[i-1][j-1] = 1
                        valid_points_matrix[i-1][j] = 1
                        # current row
                        valid_points_matrix[i][j-1] = 1
        return valid_points_matrix

    @staticmethod
    def part1():
        """Part 1"""
        Day3.__schematic = 'test.txt'
        with open(Day3.__schematic, 'r') as file:
            lines = file.readlines()
        symbols = []
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            # print(lines[i])
            for l in lines[i]:
                if not l.isnumeric() and l != '.':
                    symbols.append(l)
        # print(set(symbols))
        nr = len(lines)
        nc = len(lines[0])  # max(lines, key=lambda x: len(x)
        print(f'Size of file: {nr}x{nc}')
        valid_points_matrix = Day3.get_part_points(lines=lines, nr=nr, nc=nc)
        # print(valid_points_matrix)
        sum_parts = 0
        # nums = []
        for l in range(len(lines)):
            line = lines[l]
            for i in Day3.__symbols:
                line = line.replace(i, '.')
            print(line)
            nums = []
            for n in line.split('.'):
                if n.isnumeric() and n not in nums:
                    nums.append(n)
            parts = []
            for n in nums:
                j = 0
                while True:
                    i = line.find(n, j)
                    if i == -1:
                        break
                    else:
                        if sum(valid_points_matrix[l, i:(i+len(n))]) > 0:
                            parts.append(int(n))
                        print(valid_points_matrix[l, i:(i+len(n))])
                    j = i+1
            sum_parts += sum(parts)
            print(f'{l+1}:', parts)
        print('Sum of parts:', sum_parts)
        return sum_parts


if __name__ == '__main__':
    Day3.part1()  # 535203, 533097 , 542390 <- too low, 559887, 550594 <- not right
