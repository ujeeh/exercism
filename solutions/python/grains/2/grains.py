''' Finding the total amount of grains in any given square
and also on the total board
'''
FIRST_SQUARE = 1
RATIO = 2
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    number_of_grains = FIRST_SQUARE * RATIO ** (number - 1)
    return number_of_grains


def total():
    chess_squares = 64
    total_sum = FIRST_SQUARE * (RATIO ** (chess_squares) - 1)//(RATIO - 1)
    return int(total_sum)
