'''Day 7 Advent of Code 2022
@author: Gemma McLean
Github: gemixin
Credits:
I struggled to find the best way to approach this one. Huge thanks to
Coding with Krp Ajay for his brilliant breakdown of the problem, which inspired
my solution below. YouTube link:
https://www.youtube.com/watch?v=wdzsEOpyOUo&list=PL6j4z1hi1vaavMKehcfJSt6T4zC_ITmsA&index=6
'''
from collections import defaultdict

# Read the file in to a list of strings
with open('day7/input.txt') as file_object:
    list_lines = [line.strip() for line in file_object.readlines()]

# Create an empty list to store each folder name in the current directory
dir_stack = []
# Create an empty default dictionary (0 default value) to store the total filesize
# for each directory
filesizes = defaultdict(int)

# Process each line of input
for line in list_lines:
    # Split the line
    split_line = line.split()
    # If it's a command
    if (split_line[0] == '$'):
        # If it's a cd command (ignore ls commands)
        if (split_line[1] == 'cd'):
            # If the new directory is the root:
            if (split_line[2] == '/'):
                # The directory stack would only consist of the root element
                dir_stack = ['/']
            # If the new directory is a level up (via the .. command)
            elif (split_line[2] == '..'):
                # Pop the last element in the directory stack
                dir_stack.pop()
            # Otherwise, append the new directory to the stack
            else:
                dir_stack.append(split_line[2])
    # If it's not a command then it's output
    else:
        # If it's a file (ignore directories)
        if (split_line[0] != 'dir'):
            # Add the filesize to the current directory and for each directory beneath
            # it in the stack
            current_path = ''
            for dir in dir_stack:
                current_path += dir
                filesizes[current_path] += int(split_line[0])

'''Part One'''
# Answer is the sum of the directory sizes where a directory is less than 100000
print(sum([val for val in filesizes.values() if val < 100000]))

'''Part Two'''
# Total device space
total_space = 70000000
# Required free space
req_space = 30000000
# Current free space
current_space = total_space - filesizes['/']
# The amount of space we need to free up
del_space = req_space - current_space
# Answer is the smallest directory of the directories that are big enough to free up
# the needed space
print(min([val for val in filesizes.values() if val >= del_space]))
