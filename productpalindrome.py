#how to check if num is palindrome
#product = left * right
#track/find largest 
#generate pairs for left and right
def palindromechecker(word):
    
    i = 0
    j = len(word) - 1
    while i<j:
        if word[i]!= word[j]:
            return False

        i += 1
        j -= 1
    #end of while loop
    return True

largest = 0
for left in range(100, 1000):
    for right in range(100, 1000):
        product = left * right
        #if str(product) == str(product)[::-1]:
        #comparing 2 strings
        #reversing a string
        #comparing equality of 2 int
        
        productstring = str(product)
        if palindromechecker(productstring) == True:
            largest = max(largest, product)
            

print(largest)