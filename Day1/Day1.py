"""
@author Karol K
@date 01/12/2023
"""

calibration_file = 'Day1/calibration_file.txt'
numbers = {'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9}

def part1():
    """Part 1"""
    cal_values_sum = 0
    with open(calibration_file, 'r') as file:
        lines = file.readlines()
        for i in lines:
            nums = [int(j) for j in i if j.isnumeric()]
            cal_value = int(f'{nums[0]}{nums[-1]}')
            cal_values_sum += cal_value
            # print(i[:-1], nums) if i[-1] == '\n' else print(i, nums)
    print('Sum of calibration values:', cal_values_sum)
    return cal_values_sum

def part2():
    """Part 2"""
    cal_values_sum = 0
    # calibration_file = 'test.txt'
    with open(calibration_file, 'r') as file:
        lines = file.readlines()
        for i in lines:
            nums = [(int(i[j]), j) for j in range(len(i)) if i[j].isnumeric()]
            for k in numbers.keys():
                if k in i:
                    it = 0
                    while True:
                        j = i.find(k, it)
                        if j == -1:
                            break
                        else:
                            nums.append((numbers[k], j))
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
    part2()  # 54498
