"""
@author Karol K
@date 14/12/2023
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


input_file = 'Day9/input.txt'


def part1():
    """9.1"""
    print('AoC23: 9.1')
    print('----------')
    with open(input_file, 'r') as file:
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
    part1()
