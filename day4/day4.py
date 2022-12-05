'''Day 4 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

# Read the file in to a nested list
# Each sublist contains a pair of elves which are sublists themselves
# containing the start and end range numbers for that elf
with open('day4/input.txt') as file_object:
    section_pairs = []
    for line in file_object.read().split('\n'):
        section_pairs.append([val.split('-') for val in line.split(',')])

'''Part One'''
# Loop through the pairs of elves to find complete overlaps
complete_overlaps = 0
for pair in section_pairs:
    # if elf1_start is less than or equal to elf2_start...
    # ...which is less than or equal to elf2_end...
    # ...which is less than or equal to elf1_end -> overlap
    if (int(pair[0][0]) <= int(pair[1][0]) <= int(pair[1][1]) <= int(pair[0][1])):
        complete_overlaps += 1
    # or if elf2_start is less than or equal to elf1_start...
    # ...which is less than or equal to elf1_end...
    # ...which is less than or equal to elf2_end -> overlap
    elif (int(pair[1][0]) <= int(pair[0][0]) <= int(pair[0][1]) <= int(pair[1][1])):
        complete_overlaps += 1

# Answer is number of overlaps
print(complete_overlaps)

'''Part Two'''
# Loop through the pairs of elves to find partial overlaps
partial_overlaps = 0
for pair in section_pairs:
    # if elf1_start is less than or equal to elf2_start...
    # ...which is less than or equal to elf1_end -> overlap
    if (int(pair[0][0]) <= int(pair[1][0]) <= int(pair[0][1])):
        partial_overlaps += 1
    # if elf2_start is less than or equal to elf1_start...
    # ...which is less than or equal to elf2_end -> overlap
    elif int(pair[1][0]) <= int(pair[0][0]) <= int(pair[1][1]):
        partial_overlaps += 1

# Answer is number of new overlaps
print(partial_overlaps)
