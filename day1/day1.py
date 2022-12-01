'''Day 1 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

# Read the file in to a list of lists
# Each sublist contains each individual elf calorie entries
with open('day1/input.txt') as file_object:
    # List comprehension version
    # input = [[int(val) for val in x] for x in [section.split() for section in
    #                                            file_object.read().split('\n\n')]]

    # More readable version with for loop
    calories = []
    for section in file_object.read().split('\n\n'):
        calories.append([int(val) for val in section.split()])

# Sum up each sublist
sums = [sum(sub_list) for sub_list in calories]

'''Part One'''
# Answer is the max of the list of sums
print(max(sums))

'''Part Two'''
# Answer is the sum of the highest 3 numbers in the list of sums
print(sum(sorted(sums)[-3:]))
