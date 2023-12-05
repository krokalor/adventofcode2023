"""
@author Karol K
@date 01/12/2023
"""

class Day1:
    ''''Class containing day 1 solutions'''

    __calibration_file = 'calibration_file.txt'
    __numbers = {'one': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4,
                 'five': 5,
                 'six': 6,
                 'seven': 7,
                 'eight': 8,
                 'nine': 9}

    def __init__(self):
        """Empty constructor"""

    @staticmethod
    def part1():
        """Part 1"""
        print('Part 1')
        cal_values_sum = 0
        with open(Day1.__calibration_file, 'r') as file:
            lines = file.readlines()
            for i in lines:
                nums = [int(j) for j in i if j.isnumeric()]
                cal_value = int(f'{nums[0]}{nums[-1]}')
                cal_values_sum += cal_value
                # print(i[:-1], nums) if i[-1] == '\n' else print(i, nums)
        print('Sum of calibration values:', cal_values_sum)
        return cal_values_sum

    @staticmethod
    def part2():
        """Part 2"""
        print('Part 2')
        cal_values_sum = 0
        # Day1.__calibration_file = 'test.txt'
        with open(Day1.__calibration_file, 'r') as file:
            lines = file.readlines()
            for i in lines:
                nums = [(int(i[j]), j) for j in range(len(i)) if i[j].isnumeric()]
                for k in Day1.__numbers.keys():
                    if k in i:
                        it = 0
                        while True:
                            j = i.find(k, it)
                            if j == -1:
                                break
                            else:
                                nums.append((Day1.__numbers[k], j))
                                it = j+1
                nums.sort(key=lambda x: x[1])
                nums_vals = [i[0] for i in nums]
                cal_values_sum += int(f'{nums_vals[0]}{nums_vals[-1]}')
                if i[-1] == '\n':
                    print(i[:-1], nums, nums_vals, int(f'{nums_vals[0]}{nums_vals[-1]}'), cal_values_sum)
                else:
                    print(i, nums, nums_vals, int(f'{nums_vals[0]}{nums_vals[-1]}'), cal_values_sum)
        print('Sum of calibration values:', cal_values_sum)
        return cal_values_sum


if __name__ == '__main__':
    Day1.part2()  # 54498
