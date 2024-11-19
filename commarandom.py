from random import randrange
def csv_to_list(text):
    '''convert a string with numerics seperated by commas to a list of integers

    argument
        text: a string csv

    return
        list: list of int
    '''
    csv = text.split(',')
    a_list = []

    for item in csv:
        a_list.append(int(item))

    ##return [int(item) for item in text.split(',')]


def rand_list(start, end, freq):
    if start < end and freq > 0:
        a_list = []
        for _ in range(freq):
            new_value = randrange(start, end+1)
            a_list.append(new_value)
        return a_list
    else:
        return[]

print(csv_to_list("1,2,3,4,5"))
print(rand_list(1, 1000, 30))

