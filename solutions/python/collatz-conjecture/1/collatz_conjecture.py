def steps(number):
    count = 0
    new_number = number
    if new_number < 1:
            raise ValueError('Only positive integers are allowed')
    while new_number != 1:
        if new_number % 2 == 0:
            new_number = new_number // 2
        else:
            new_number = (new_number * 3) + 1
        count += 1            
    return count