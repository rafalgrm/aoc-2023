import re

with open("/workspaces/aoc-2023/1/input.txt", "r") as input:
    lines = [line.rstrip('\n') for line in input.readlines()]

    sum = 0
    for line in lines:
        digits = [letter for letter in line if letter.isdigit()]
        number = (10 * int(digits[0])) + int(digits[-1])
        sum += number

    print(sum)

def get_number(text):
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    first_digit_pattern = re.compile(r'(1|2|3|4|5|6|7|8|9|' + "|".join(digits_dict.keys()) + r')')
    last_digit_pattern = re.compile(r'(1|2|3|4|5|6|7|8|9|' + "|".join([key[::-1] for key in digits_dict.keys()]) + r')')
    first_digit_str = first_digit_pattern.search(text).group(0)
    last_digit_str = last_digit_pattern.search(text[::-1]).group(0)

    first_digit = first_digit_str if first_digit_str.isdigit() else digits_dict[first_digit_str]
    last_digit = last_digit_str if last_digit_str.isdigit() else digits_dict[last_digit_str[::-1]]

    return (10 * int(first_digit)) + int(last_digit)

with open("/workspaces/aoc-2023/1/input.txt", "r") as input:
    lines = [line.rstrip('\n') for line in input.readlines()]

    sum = 0
    for line in lines:
        sum += get_number(line)

    print(sum)