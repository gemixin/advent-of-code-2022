'''Day 6 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

# Read the file in to a single string
with open('day6/input.txt') as file_object:
    datastream = file_object.read().strip()


def findMarker(datastream, n):
    '''Returns the index of the char after the first n unique chars'''
    # Starting at the nth char, loop through the chars in the string
    for i in range(n, len(datastream)):
        # Convert each block of the previous n chars to a set
        # If the length of the set is n, it means all the chars in this block are unique
        if (len(set(datastream[i-n:i])) == n):
            # Therefore our marker index is i
            return i


'''Part One'''
# Answer is the index at which the first marker occurs (after 4 unique chars)
print(findMarker(datastream, 4))

'''Part Two'''
# Answer is the index at which the first marker occurs (after 14 unique chars)
print(findMarker(datastream, 14))
