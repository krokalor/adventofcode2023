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
        Day4.__cards = 'test.txt'
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
            for j in winning_numbers:
                if f' {j} ' in f' {numbers[1]} ':
                    points = 2**p
                    p += f' {numbers[1]} '.count(f' {j} ')
            print(f'Points = {points}')
            total_points += points
        print(f'Total points = {total_points}')
        return total_points

    @staticmethod
    def part2():
        """Part 1"""
        # Day4.__cards = 'test.txt'
        with open(Day4.__cards, 'r') as file:
            lines = file.readlines()
        cards = {}
        for l in lines:
            c = l.split(':')
            cards[c[0]] = c[1].strip()
        points = {}
        for i in cards.keys():
            print(f'{i}: {cards[i]}')
            numbers = cards[i].split('|')
            winning_numbers = numbers[0].split()
            print(f'Winning numbers: {winning_numbers}')
            points[i] = 0
            matches = []
            for j in winning_numbers:
                if f' {j} ' in f' {numbers[1]} ':
                    points[i] += 1
                    matches.append(j)
            print(f'Points = {points[i]}, matches = {matches}\n')
        for i in points:
            print(f'{i}: {points[i]} copies')
        print()
        multiplier = [1]*len(points)
        k = 0
        for i in points.values():
            j = 0
            while True:
                if j == i or k + j == len(multiplier)-1:
                    k += 1
                    break
                else:
                    j += 1
                    multiplier[k+j] += multiplier[k]
            card_number = sum(multiplier)
            print(multiplier, card_number)
        print(f'Final card number: {card_number}')
        return card_number


if __name__ == '__main__':
    Day4.part2()
