def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.lower().split()
    newPhrase = list()
    newWord = ""

    for word in phrase:

        newWord = (word[0].upper())
        newWord = newWord + (word[1:])
        newPhrase.append(newWord)

    return (" ").join(newPhrase)