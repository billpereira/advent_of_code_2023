import re

# Reading Input file
input_file = open("day1_input", "r")
calibration_file = input_file.readlines()

# Creating a table of conversion for the spelled numbers
convert_table = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

sum = 0

def get_calibration_digits(calibration_line, current_sum):
    # Regex with lookahead adding the numbers as they are spelled to allow find them together with numeric digit
    digits_of_line = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))',calibration_line)
    print(digits_of_line)
    # Changing them using the convert table in case they are as spelled
    first_digit = digits_of_line[0] if len(digits_of_line[0]) == 1 else convert_table[digits_of_line[0]]
    last_digit = digits_of_line[-1] if len(digits_of_line[-1]) == 1 else convert_table[digits_of_line[-1]]
    calibration_value = first_digit+last_digit
    current_sum = current_sum + int(calibration_value)
    return current_sum

# Loop through the input file
for line in calibration_file:
    sum = get_calibration_digits(line, sum)
    print(sum)