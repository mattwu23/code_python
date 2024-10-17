def consonant_counter(text, vowel=False):
    ''' returns the number of consonants in a given string
    argument
        text: a string value containing alphamaric characters and special symbols
        vowel: it is assumed to be false when counting for consonants

    returns
        an int: total count of all consonants in text
    '''
    ctr = 0 #for consonants

    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
            ctr+=1

    if not vowel:
        #not interested in counting vowels
        return ctr
    else:
        ctr = 0
        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a', 'e', 'i', 'o', 'u'}:
                ctr+=1

print(f'the count is {consonant_counter('hello, world')}')
print(f'the count is {consonant_counter('hello, world', True)}')