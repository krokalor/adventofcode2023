"""
@author Karol K
"""

# from string import whitespace
import numpy as np
# from termcolor import colored
import time
import math


def directions(s):
    """Generator for directions (converts L->0 and R->1)"""
    while True:
        for i in s:
            yield int(i)

def find_period():
    d = directions(s)


def part1(input_file):
    """8.1"""
    print('AoC23: 8.1\n')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    instruction = lines[0].strip().replace('L', '0').replace('R', '1')
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


def path_period(node, nodes, instruction):
    step = 1
    print('-'*10,node,'-'*10)
    d = directions(instruction)
    while True:
        i = next(d)
        node = nodes[node][i]
        if node.endswith('Z'):
            return step
        step += 1


def part2(input_file):
    """8.2"""
    with open(input_file, 'r') as file:
        lines = file.readlines()
    instruction = lines[0].strip().replace('L', '0').replace('R', '1')
    print('Instruction, [L]eft/[R]ight:', instruction)
    nodes = {i[0]: i[1][1:-1].split(', ') for i in [line.strip().split(' = ') for line in lines[2:]]}
    paths = [p for p in nodes if p.endswith('A')]
    paths_number = len(paths)
    periods = []
    for i in range(len(paths)):
        periods.append(path_period(paths[i], nodes, instruction))
    print(f'Number of steps equal to lowest common multiple of periods: {math.lcm(*periods):d}')


if __name__ == '__main__':
    # part1('Day8/input.txt')
    part2('Day8/input.txt')
