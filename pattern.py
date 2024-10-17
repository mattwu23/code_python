def create_line(num):
    '''returns a string of 1 and 0 based on the argument

    arguemtn:
        num: integer, to determine how long the string is

    return:
        text: series of 1 and 0
    '''
    text = ''
    for i in range(1, num+1): # example if num is 5, range (1,6) ----- (1,2,3,4,5)
        if i%2 == 0:
            text += '0'
        else:
            text += '1'

    return text
    #end create_line()
def output_pattern(num):
        
    for i in range(1, num+1):
        print(create_line(i))

v = output_pattern(10)

