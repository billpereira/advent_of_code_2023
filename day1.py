import re

# Reading Input file
input_file = open("day1_input", "r")
calibration_file = input_file.readlines()

# Creating a table of conversion, keeping the word as with a hard replace it
# will sometimes loose numbers if the words overlap i.e. eightwo
convert_table = {
    'one':'on1e',
    'two':'tw2o',
    'three':'thr3ee',
    'four':'fo4ur',
    'five':'fiv5e',
    'six':'si6x',
    'seven':'sev7en',
    'eight':'eig8ht',
    'nine':'ni9ne'
}

sum = 0

def get_calibration_digits(calibration_line, current_sum):
    digits_of_line = re.findall('[\d]',calibration_line)
    first_digit = digits_of_line[0]
    last_digit = digits_of_line[-1]
    calibration_value = first_digit+last_digit
    current_sum = current_sum + int(calibration_value)
    return current_sum

for line in calibration_file:
    for key,value in convert_table.items():
        line = line.replace(key, value)
    sum = get_calibration_digits(line, sum)
    print(sum)