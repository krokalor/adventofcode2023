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
        print('AoC23: 9.1')
        print('----------')
        Day9.__input = 'test.txt' if test else Day9.__input
        with open(Day9.__input, 'r') as file:
            lines = file.readlines()
        history = []
        for line in lines:
            history.append([int(i) for i in line.split()])
        print(history)
        print()
        ex_sum = 0
        for h in history:
            diff = [h]
            while True:
                # print(h)
                if sum(h) == 0:
                    break
                else:
                    h = list(np.diff(h))
                    diff.append(h)
            diff[-1].append(0)
            print(diff[-1])
            for i in range(len(diff)-1)[::-1]:
                diff[i].append(diff[i][-1]+diff[i+1][-1])
                print(diff[i])
            ex = diff[0][-1]
            ex_sum += ex
            print(ex, ex_sum)
            print()


if __name__ == '__main__':
    Day9.part1(False)
