def is_divisible(num1, num2):
    ''' checks if num1 is divisble by num2

    Args:
        num1: integer, numerator
        num2: integer, demoninator

    Return:
        True if num1 is dvisibile by num2, otherwise false
    '''
    return num1%num2
#end of is_divisible
def factor_count(number):
    '''determines the number of factors the argument has
    
    Args: 
        number: an integer needed to determine the number of it's factors
    
    Returns:
        an integer, which is the total amount of factors the argument haskl
    '''
    counter = 0
    for divider in range(1, number+1):
        if is_divisible(number, divider)== 0:
            counter +=1
    #end of for loop
    return counter
#end of factorcount()

upper_limit = int(input("Enter N: "))

for num in range(1, upper_limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors.")