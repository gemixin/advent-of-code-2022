'''Day 8 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

import numpy as np

# Read the file in to a list of lists
# Each sublist is a row of numbers
with open('day8/input.txt') as file_object:
    rows = []
    for row in file_object.read().split('\n'):
        rows.append([int(val) for val in row])

# Convert to a numpy array
grid = np.array(rows)
# Work out the grid size
grid_size = grid.shape[0]

'''Part One'''
# Get the number of trees around the edge -> these are all visible
visible = (grid_size-1)*4
# Loop through all the inner numbers in the grid (ignore edge)
for i, row in enumerate(grid[1:grid_size-1]):
    for j, tree_height in enumerate(row[1:grid_size-1]):
        # Check if the tree is visible
        # Slice the grid to get the rows of other trees in each direction
        # Order = right, left, down, up
        slices = [grid[i+1, j+2:], grid[i+1, :j+1], grid[i+2:, j+1], grid[:i+1, j+1]]
        # Loop through the slices
        for slice in slices:
            # See if the current tree is taller than the tallest tree in each slice
            if (tree_height > max(slice)):
                # If it's visible from at least one direction
                visible += 1
                break

# Answer is the total number of visible trees
print(visible)

'''Part Two'''
# Loop through all the numbers in the grid
# Set the max scenic score to 0
max_scenic_score = 0
# Loop through all the numbers in the grid
for i, row in enumerate(grid):
    for j, tree_height in enumerate(row):
        # Slice the grid to get the rows of other trees in each direction
        # Reverse the left and up slices to reflect the direction from the current tree
        # Order = right, left, down, up
        slices = [grid[i, j+1:], np.flip(grid[i, :j]),
                  grid[i+1:, j], np.flip(grid[:i, j])]
        # Create an empty list to store the number of visible trees in each direction
        # for the current tree
        visible = []
        # Loop through the slices
        for slice in slices:
            # Get an array of the indexes of all blocking trees for the current
            # direction
            blocking_trees = np.argwhere(slice >= tree_height)
            # If there are any blocking trees...
            # To find the number of visible trees we want the index of the first
            # blocking tree plus 1 (i.e. if the index is 2, it means the first
            # blocking tree is 3 away)
            if (len(blocking_trees) > 0):
                visible.append(int(blocking_trees[0]) + 1)
            # If there are no blocking trees, the number of visible trees is equal to
            # the length of the slice (i.e. the number of trees to the edge in the
            # current direction)
            else:
                visible.append(len(slice))
        # The scenic score for the current tree is the number of visible trees
        # multiplied together
        # If it's bigger than the current biggest score, set it
        if np.prod(visible) > max_scenic_score:
            max_scenic_score = np.prod(visible)

# Answer is the largest scenic score
print(max_scenic_score)
