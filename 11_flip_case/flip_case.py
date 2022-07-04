def flip_case(phrase, to_swap):
    upper_copy = str(to_swap)
    lower_copy = str(to_swap)
    upper_copy = upper_copy.upper()
    lower_copy = lower_copy.lower()
    new_word = ''

    for letter in phrase:
        if letter == upper_copy:
            new_word = new_word + letter.lower()
            print(new_word)
        elif letter == lower_copy:
            new_word = new_word + letter.upper()
        else:
            new_word = new_word + letter
    return new_word


    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
