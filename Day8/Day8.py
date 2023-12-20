"""
@author Karol K
@date 14/12/2023
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


class Day8:
    __input = 'input.txt'
    __dir = {'L': 0, 'R': 1}

    @staticmethod
    def directions(s):
        """Generator for directions (converts L->0 and R->1)"""
        # TODO: read more about generators
        while True:
            for i in s:
                yield Day8.__dir[i]

    @staticmethod
    def part1(test=True):
        """8.1"""
        print('AoC23: 8.1\n')
        Day8.__input = 'test.txt' if test else Day8.__input
        with open(Day8.__input, 'r') as file:
            lines = file.readlines()
        instruction = lines[0].strip()
        print('Instruction, [L]eft/[R]ight:', instruction)
        nodes = {i[0]: i[1][1:-1].split(', ') for i in [line.strip().split(' = ') for line in lines[2:]]}
        print('Nodes:')
        for n in nodes:
            print(f'{n}: {nodes[n]}')
        print()
        ##
        d = Day8.directions(instruction)
        n = 'AAA'
        step = 1
        while True:
            print(step, n, nodes[n])
            n = nodes[n][next(d)]
            if n == 'ZZZ':
                print(f'{step} {n}!!!')
                break
            else:
                step += 1
        print('Number of steps:', step)


if __name__ == '__main__':
    Day8.part1(False)
