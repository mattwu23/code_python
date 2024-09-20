#this code takes users input for first name, last name, and year they were born
#output the first name
#output the last name
#output the users age
#output if they are able to drink in ontario

firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
year = int(input("What year were you born? "))
difference = 2024-year
print (firstname)
print (lastname)
print ("You are", difference, "years old")

if difference<19 :
    print("You are not old enough to drink")
else :
    print("You are old enough to drink")