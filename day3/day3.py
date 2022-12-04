'''Day 3 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''
import string

# Read the file in to a list of strings
with open('day3/input.txt') as file_object:
    list_lines = [line.strip() for line in file_object.readlines()]

# A string of letters a-z and A-Z
alphabet = string.ascii_lowercase + string.ascii_uppercase
# A dictionary of priority values for each letter (a=1 -> Z=52)
letter_values = {alphabet[i]: i+1 for i in range(0, len(alphabet))}

'''Part One'''
# Create a list of tuples that contains two strings (each input string halved)
backpacks = [(line[:len(line)//2], line.strip()[len(line)//2:])
             for line in list_lines]
# Create a list of letters that are present in both strings in each tuple
common_letters = [''.join(set(s1).intersection(s2)) for s1, s2 in backpacks]
# Answer is the sum of the letter values for each of the common letters
print(sum([letter_values[letter] for letter in common_letters]))

'''Part Two'''
# Create a list of lists where each sublist contains three strings
groups_of_three = [list_lines[i:i+3] for i in range(0, len(list_lines), 3)]
# Create a list of letters that are present in all three strings in each group of 3
new_common_letters = [''.join(set(s1).intersection(s2, s3))
                      for s1, s2, s3 in groups_of_three]
# Answer is the sum of the letter values for each of the new common letters
print(sum([letter_values[letter] for letter in new_common_letters]))
