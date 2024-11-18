def dupcharacters (word1, word2):
    ''' returns the characters that are found in both words

    arguments:
    word1: string value... expected alphamaric value all lowercase
    word2: string value... expected alphamaric value all lowercase

    return:
    a list of the shared characters in both words
    '''
    if not word1 or not word2:
        return[]
    else:
        set_word1 = set(word1)
        set_word2 = set(word2) #creates a set with no dupes
        
        result = []

        for character in set(word1):
            if character in set_word2:
                result.append(character)
        return sorted(result)

print (dupcharacters('hello world', 'goodbye world'))