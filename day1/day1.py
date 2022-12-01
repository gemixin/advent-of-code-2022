'''Day 1 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

# Read the file in to a list of lists
# Each sublist contains each individual elf calorie entries
with open('day1/input.txt') as file_object:
    input = [[int(val) for val in x] for x in [section.split() for section in
                                               file_object.read().split('\n\n')]]

# Sum up each sublist
sums = [sum(val) for val in input]

'''Part One'''
# Answer is the max of the list of sums
print(max(sums))

'''Part Two'''
# Answer is the sum of the highest 3 numbers in the list of sums
print(sum(sorted(sums)[-3:]))
