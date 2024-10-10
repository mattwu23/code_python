# turn an arg into a string
# look through each character of the string, grab only alpha characters or remove non-alpha characters
#grow an empty string to a string filled with alphabetical characters
#string method used: isalpha(), returns true if the string has only letter characters from the ASCII table

def string_cleaner(text):
    ''' to clean a string with non alpha characters and put them all in lowercase

    arguements
        text: a string to be cleaned

    returns
        a string object with only alphabetical lowercased character
    '''
    result = ' '
    for character in text:
        #since strings are immutable, cannot mutate and remove characters unwanted characters
        #print(character)
        if character.isalpha():
            #result = result+character.lower()
            result += character.lower() 
            #.lower makes string all lower case
            # + operator combines strings

    return result
#end of string_cleaner()

value = string_cleaner("123456uyhjbnvc iuytrewts546tyv jin hy6cy uvt6x5ytug jkuj jb ")
print(f"Value is {value}")
