def isPalindrome(word):
    #base case 1: empty strings are palindrome
    if not word:
        return True
    elif len(word)==1:
        #1 letter is a palindrome
        return True
    elif len(word)<=3:
        return word[0]==word[-1]
    else:
        #complicated, long word
        #flipped = word[::-1]#reverses a sliceable object
        #return word == flipped
        i = 0
        j = len(word) - 1
        while i<j:
            if word[i]!= word[j]:
                return False

            i += 1
            j -= 1
        #end of while loop
        return True 

print(isPalindrome('cac'))
       
            