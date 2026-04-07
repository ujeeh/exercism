def response(hey_bob):
    reply = 'Whatever'
    # strip all the whitespace from the sentence to determine if its silence or a pause
    hey_bob = hey_bob.strip( )
    # if statement ends in question mark
    is_question = hey_bob.endswith('?')
    # if statement seems loud (all caps)
    is_yelling = hey_bob.isupper()
    # we have to specify when a condition is not met as there are scenarios where there are two conditions and just one condition will trigger the function.
    if is_question and not is_yelling:
        reply = 'Sure.'
    elif is_yelling and not is_question:
        reply = 'Whoa, chill out!'
    elif is_question and is_yelling:
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob == '':
        reply ='Fine. Be that way!'
    else:
        reply = 'Whatever.'
    return reply
    pass
