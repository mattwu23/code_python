def is_palindrome1(text):
    '''checks if our given argument is a palindrome

    argument
        text: an alphabetical based string

    return
        a boolean value, True if the text is a palindrome, False otherwise
    '''
    return text == text[::1]
#end of is_palindrome()

#solution 2: determining the midpoint then checking to see if the other end is the same
def is_palindrome2(text):
    '''checks if our given argument is a palindreom

    argument
        text: an alphabetical based string

    return
        a boolean value, True if the text is a palindrome, False otherwise
    '''
    if not text:
        #text is an empty string
        return True
    elif len(text)<4:
        #for strings with lengths of 1,2,3... as long as the first and last characters are the same 
        #it is a plaindrome
        return text[0] == text[-1]
    else:
        #our text is now guaranteed of 4+ length
        midpoint = len(text) //2
        #if length is odd/ ignore the middle character
        #01234 - length of 5
        #Hello

        #0123 - length of 4
        for i in range(0, midpoint):
            left = text[i]
            right = text [-1*i-1]
            #i=0, -1
            #i=1, i=-2
            if left != right:
                return False #return in loop is a break
#end of for loop
        return True
print(is_palindrome1('tacocat'), is_palindrome2('tacocat'))
print(is_palindrome1('tacodog'), is_palindrome2('tacodog'))