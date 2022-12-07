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


def moveCrates(stacks, instructions, rev=True):
    '''Process the instructions and rearrange the crates in the stacks accordingly'''
    for i in instructions:
        # Get the crates that need to be moved
        crates_to_move = stacks[i[1]][-i[0]:]
        # Remove crates from outgoing stack by shrinking that stack
        stacks[i[1]] = stacks[i[1]][:-i[0]]
        # Add crates to incoming stack
        # If moving one by one, reverse the list (part one)
        if (rev):
            stacks[i[2]].extend(reversed(crates_to_move))
        # Otherwise, simulate moving entire block at once (part two)
        else:
            stacks[i[2]].extend(crates_to_move)


'''Part One'''
stacks1 = copy.deepcopy(stacks)
moveCrates(stacks1, instructions)
# The answer is the string concatenation of the letters on top of each stack
print(''.join([stack[-1] for stack in stacks1]))

'''Part Two'''
stacks2 = copy.deepcopy(stacks)
moveCrates(stacks2, instructions, rev=False)
# The answer is the string concatenation of the letters on top of each stack
print(''.join([stack[-1] for stack in stacks2]))
