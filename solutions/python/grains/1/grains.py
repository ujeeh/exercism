FIRST_SQUARE = 1
RATIO = 2
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    number_of_grains = FIRST_SQUARE * RATIO ** (number - 1)
    return number_of_grains


def total():
    CHESS_SQUARES = 64
    total = FIRST_SQUARE * (RATIO ** (CHESS_SQUARES) - 1)//(RATIO - 1)
    return int(total)
