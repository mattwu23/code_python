def anagram(text1, text2):
    ''' returns if the 2 words are anagrams or not
    
    arguments: 
    text1: a string value
    text2: a string value

    return:
    returns True if arguements are anagrams, False if not
    '''
    if len(text1) != len(text2):
        return False 
    else:
        # look through all letters
        for character in text1:
            if text1.count(character) != text2.count(character):
                return False
        return True

result1 = anagram("bored", "robed")
result2 = anagram("jake", "jasper")
result3 = anagram("cinema", "iceman")

print (result1, result2, result3)