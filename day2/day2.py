'''Day 2 Advent of Code 2022
@author: Gemma McLean
Github: gemixin'''

'''
A and X = Rock (1 point)
B and Y = Paper (2 points)
C and Z = Scissors (3 points)

Win = 6 points
Draw = 3 points
Loss = 0 points
'''

# Read the file in to a list of lists
# Each sublist is a round that contains the opponent's choice and my choice
with open('day2/input.txt') as file_object:
    rounds = [line.split(' ') for line in file_object.read().split('\n')]

# Points values for each choice
point_values = {'X': 1, 'Y': 2, 'Z': 3}
# Dictionary of result combinations (format = [win, draw, loss])
result_combos = {'A': ['Y', 'X', 'Z'], 'B': ['Z', 'Y', 'X'], 'C': ['X', 'Z', 'Y']}
# Point values for win, draw, loss
result_points = [6, 3, 0]


def calculate_scores(rounds):
    '''Calculate the score for each round'''
    return [result_points[result_combos[opponent].index(me)] + point_values[me]
            for opponent, me in rounds]


'''Part One'''
# Answer is the sum of the round scores
round_scores = calculate_scores(rounds)
print(sum(round_scores))

'''Part Two'''
# Create a new list using the same format as part one, based on whether or not a win,
# loss or draw is needed (X = loss, Y = draw, Z = win)
required_index = {'X': 2, 'Y': 1, 'Z': 0}
new_rounds = [[opponent, result_combos[opponent][required_index[me]]]
              for opponent, me in rounds]

# Answer is the sum of the new round scores
new_round_scores = calculate_scores(new_rounds)
print(sum(new_round_scores))
