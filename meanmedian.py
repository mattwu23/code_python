def mean(a_list):
    ''' returns the mean of a list

    arguments
        a_list: list of int values

    return
        returns the int value of the mean of the list
    '''
    return sum(a_list) / len(a_list)

def median(a_list):
    ''' returns the median in a dataset

    arguments
        a_list: list of int values

    return
        returns the int value of the mean of the list
    '''
    m = len(a_list) // 2 # m = midpoint
    sorted_list = sorted(a_list)

    if m % 2 == 0:
        left = sorted_list[m-1]
        right = sorted_list[m]
        average = (left+right)/2
        return average
    else:
        return sorted_list[m]

from random import seed
from random import randrange

seed(1)
data = [randrange(1,100) for _ in range(randrange(10,30))]

print(f'the data set is {data}')
print (f'the mean is {mean(data)}')
print (f'the median is {median(data)}')