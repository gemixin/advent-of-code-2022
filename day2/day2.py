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


def calculate_scores(rounds):
    ''' Calculate the round scores'''
    round_scores = []
    for opponent, me in rounds:
        round_score = 0
        # Get the result as either 0, 1 or 2
        result = result_combos[opponent].index(me)
        # Win
        if result == 0:
            round_score += 6
        # Draw
        elif result == 1:
            round_score += 3
        # Loss -> no action as score would be 0
        # Add point value of the shape you chose
        round_score += point_values[me]
        # Add the round score to the list
        round_scores.append(round_score)
    return round_scores


'''Part One'''
# Answer is the sum of the round_scores
round_scores = calculate_scores(rounds)
print(sum(round_scores))

'''Part Two'''
# Create a new list using the same format as part one, based on whether or not a win,
# loss or draw is needed
new_rounds = []
for opponent, me in rounds:
    # If a loss is needed, select the choice at index 2
    if me == 'X':
        new_me = result_combos[opponent][2]
    # If a draw is needed, select the choice at index 1
    elif me == 'Y':
        new_me = result_combos[opponent][1]
    # If a win is needed, select the choice at index 0
    elif me == 'Z':
        new_me = result_combos[opponent][0]
    new_rounds.append([opponent, new_me])

# Answer is the sum of the new round_scores
new_round_scores = calculate_scores(new_rounds)
print(sum(new_round_scores))
