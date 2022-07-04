def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    subset = ''
    vowels = "aeiouyAEIOUY"
    for letter in s:
        if letter in vowels:
            subset = subset + letter

    subset = subset[::-1]
    new_s = ''
    i = 0
    x = 0
    while i < len(s):
        if s[i] in vowels:
            new_s = new_s + subset[x]
            x = x + 1
            i = i + 1
        else:
            new_s = new_s + s[i]
            i = i + 1
    return new_s

