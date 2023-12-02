
import re

# Reading Input file
input_file = open("day2_input", "r")
games_file = input_file.readlines()

possible_counter = 0

total_blue = 14
total_red = 12
total_green = 13
total_power = 0
for i,line in enumerate(games_file):
    possible_matches = True
    highest_blue = max([int(n) for n in re.findall('\\b(\d+) blue',line)])
    highest_green = max([int(n) for n in re.findall('\\b(\d+) green',line)])
    highest_red = max([int(n) for n in re.findall('\\b(\d+) red',line)])
    # Part 1 solution
    if highest_blue <= total_blue and highest_green <= total_green and highest_red <= total_red:
        possible_counter = possible_counter + (i+1)

    # Part 2 Solution:
    line_power = highest_green*highest_blue*highest_red
    total_power = total_power + line_power
    
    
print(f'Solution 1:{possible_counter}')
print(f'Solution 2:{total_power}')