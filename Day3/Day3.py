"""
@author Karol K
@date 01/12/2023
"""

# from string import whitespace
import numpy as np
from termcolor import colored


class Day3:
    """Day 3 solutions"""
    __schematic = 'input.txt'
    __symbols = '@*/+#=$%-&'

    @staticmethod
    def get_part_points(lines, nr, nc):
        """Returns map of valid points"""
        valid_points_matrix = np.zeros((nr, nc))
        for i in range(nr):
            for j in range(nc):
                if lines[i][j] in Day3.__symbols:
                    # upper row
                    valid_points_matrix[i - 1][j - 1] = 1
                    valid_points_matrix[i - 1][j] = 1
                    valid_points_matrix[i - 1][j + 1] = 1
                    # current row
                    valid_points_matrix[i][j - 1] = 1
                    valid_points_matrix[i][j + 1] = 1
                    # lower row
                    valid_points_matrix[i + 1][j - 1] = 1
                    valid_points_matrix[i + 1][j] = 1
                    valid_points_matrix[i + 1][j + 1] = 1
        return valid_points_matrix

    @staticmethod
    def part1():
        """Part 1"""
        # Day3.__schematic = 'test.txt'
        with open(Day3.__schematic, 'r') as file:
            lines = file.readlines()
        lines = [f'.{l.strip()}.' for l in lines]  # removing end-line symbol and adding '.' at the start and the end
        nc = len(lines[0])  # max(lines, key=lambda x: len(x)
        lines = ['.'*nc] + lines + ['.'*nc]  # adding lines full of '.' at the start and the end of file
        nr = len(lines)
        print(f'Size of file: {nr}x{nc}')   # assuming #rows=#columns
        valid_points_matrix = Day3.get_part_points(lines=lines, nr=nr, nc=nc)
        # print(valid_points_matrix)
        parts = []
        # nums = []
        for l in range(len(lines)):
            line = lines[l]
            for i in Day3.__symbols:
                line = line.replace(i, '.')
            for c in range(len(line)):
                print(colored(line[c], 'red'), end='') if valid_points_matrix[l, c] == 1 else print(lines[l][c], end='')
            print(' ', end='')
            # print(line)
            nums = []
            for n in line.split('.'):
                if n.isnumeric():
                    nums.append(n)
            # line = f'.{line}.'
            parts_line = []
            j = 0
            for n in nums:
                i = line.find(f'{n}')
                if sum(valid_points_matrix[l, (j + i):(j + i + len(n))]) > 0:
                    parts_line.append(int(n))
                    print(f'({n}, {j + i}:{j + i + len(n)})', end=' ')
                else:
                    print(n, end=' ')
                line = line[i + len(n):]
                j += i + len(n)
            print(colored(f'{sum(parts_line)}', 'blue', attrs=["bold"]))
            # print(f'{l+1}:', parts)
            parts.append(sum(parts_line))
        print(parts)
        print('Sum of parts:', colored(f'{sum(parts)}', 'red', attrs=["bold"]))
        return sum(parts)


if __name__ == '__main__':
    Day3.part1()  # 535203, 533097 , 542390 <- too low, 559887, 550594 <- not right, 248999
