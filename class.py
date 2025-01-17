#Exponentiation
#write a program that evaluates the pwoer to its integeer representation
#2^4 = 2x2x2x2 = 16
def pow1(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else: #work towards base case
        return base * pow1(base, exponent -1)

print (pow1(3,5))

def pow2(base, exponent, answer=1):
    if exponent ==0:
        return answer
    else:
        return pow2(base, exponent-1, answer * base)
    
print (pow2(3,5,))

#palindrome
def is_pali(word):
    def helper(word, left, right):
        if left>right:
            return True
        elif word[left] != word[right]:
            return False
        else:
            return helper(word, left+1, right-1)
        #end of helper
    if not word:
        return True:
    elif len(word) <=3:
        return word[0] == word[-1]
    else:
        return helper(word, left=0, right=len(word)-1)