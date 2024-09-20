# Goal is to create a password generator
# Requires password length
# requires password criteria
# does it contain numbers?
# does it contain uppercase letters
# does it include special characters
# generate a password with the given constraints
# output the generated password

import random

#program introduction
print ("Welcome to our password generating app")

#set password length
pwd_length = int(input("Enter the length of the password: "))

#password criteria
lowercase = list(range(97, 123)) 
uppercase = list(range(65, 91)) #range never includes the last value
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 126))

pwd_symbols = lowercase.copy() # a list of possible characters for our password

has_upper = input("Include uppercase characters? Y/N: ")
if has_upper == "Y" or has_upper == "y":
    pwd_symbols.extend(uppercase)

has_special = input("Include special characters? Y/N: ")
if has_special == "Y" or has_special == "y":
    pwd_symbols.extend(special)

has_digits = input("Include digits? Y/N: ")
if has_digits == "Y" or has_digits == "y":
    pwd_symbols.extend(digits)

new_password = "" # empty string to hold new password

while len(new_password) != pwd_length:
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol
#end of while loop

print(f"{new_password} has been generated.")