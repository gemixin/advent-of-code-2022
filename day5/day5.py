'''Day 5 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''
import re
import copy

# Read the file in to two separate strings
with open('day5/input.txt') as file_object:
    halves = file_object.read().split('\n\n')
string_crates = halves[0]
string_instructions = halves[1]

# Process the crates string
# The last character (strip the \n) tells us the number of stacks we need
num_stacks = int(string_crates.strip()[-1:])
# Create a list of empty stacks (lists)
stacks = [[] for _ in range(num_stacks)]

# Loop through the lines of the split string, in reverse order
# Ignore the bottom row of numbers
for row in reversed(string_crates.split('\n')[:-1]):
    # Loop through every 4 characters in each line
    for col, i in enumerate(range(1, len(row)+1, 4)):
        # If it's a crate, add it to the relevant stack
        if (row[i] != ' '):
            stacks[col].append(row[i])

# Process the instructions string
# Create a list that contains lists of instructions in the format:
# [number of crates to move, stack moving from, stack moving to]
# Pull the numbers from each line using re
instructions = [re.findall(r'\d+', line) for line in string_instructions.split('\n')]
# Convert to ints and subtract 1 from the stack numbers to match indexes of stacks
instructions = [[int(inner_pair[0]), int(inner_pair[1])-1, int(inner_pair[2])-1]
                for inner_pair in instructions]

'''Part One'''
stacks1 = copy.deepcopy(stacks)
# Process instructions
for inst in instructions:
    # For every crate that needs moving
    for i in range(inst[0]):
        # Move from outgoing stack to incoming stack
        stacks1[inst[2]].append(stacks1[inst[1]].pop())

# The answer is the string concatenation of the letters on top of each stack
print(''.join([stack[-1] for stack in stacks1]))

'''Part Two'''
stacks2 = copy.deepcopy(stacks)
# Process instructions
for inst in instructions:
    # Get the crates that need to be moved
    crates_to_move = stacks2[inst[1]][-inst[0]:]
    # Remove crates from outgoing stack by shrinking that stack
    stacks2[inst[1]] = stacks2[inst[1]][:-inst[0]]
    # Add crates to incoming stack
    stacks2[inst[2]].extend(crates_to_move)

# The answer is the string concatenation of the letters on top of each stack
print(''.join([stack[-1] for stack in stacks2]))
