"""
@author Karol K
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


input_file = 'Day8/input.txt'


def directions(s):
    """Generator for directions (converts L->0 and R->1)"""
    # TODO: read more about generators
    direction = {'L': 0, 'R': 1}
    while True:
        for i in s:
            yield direction[i]


def part1():
    """8.1"""
    print('AoC23: 8.1\n')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    instruction = lines[0].strip()
    print('Instruction, [L]eft/[R]ight:', instruction)
    nodes = {i[0]: i[1][1:-1].split(', ') for i in [line.strip().split(' = ') for line in lines[2:]]}
    print('Nodes:')
    for n in nodes:
        print(f'{n}: {nodes[n]}')
    print()
    ##
    d = directions(instruction)
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
    part1()
