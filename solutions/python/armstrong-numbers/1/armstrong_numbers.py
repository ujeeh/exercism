def is_armstrong_number(number):
    character_count = len(str(number))
    number_word = str(number)
    total = 0
    for x in range(len(str(number))):
        total = total + int(number_word[x]) ** character_count
    return total == number

