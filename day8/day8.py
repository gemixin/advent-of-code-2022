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
