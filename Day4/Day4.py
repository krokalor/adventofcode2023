"""
@author Karol K
@date 05/12/2023
"""

# from string import whitespace
# import numpy as np
# from termcolor import colored


class Day4:
    """Day 4 solutions"""
    __cards = 'input.txt'

    @staticmethod
    def part1():
        """Part 1"""
        # Day4.__cards = 'test.txt'
        with open(Day4.__cards, 'r') as file:
            lines = file.readlines()
        cards = {}
        for l in lines:
            c = l.split(':')
            cards[c[0]] = c[1].strip()
        total_points = 0
        for i in cards.keys():
            print(f'{i}: {cards[i]}')
            numbers = cards[i].split('|')
            winning_numbers = numbers[0].split()
            print(f'Winning numbers: {winning_numbers}', end=', ')
            points, p = 0, 0
            for i in winning_numbers:
                if f' {i} ' in f' {numbers[1]} ':
                    points = 2**p
                    p += f' {numbers[1]} '.count(f' {i} ')
            print(f'Points = {points}')
            total_points += points
        print(f'Total points = {total_points}')
        return total_points


if __name__ == '__main__':
    Day4.part1()
