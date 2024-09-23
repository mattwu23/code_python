#import statement 
from math import ceil
#input
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

#processing 
cans = len(section1) + len(section2) + len(section3)

boxes = ceil(cans/12) #using ceil rounds up to nearest whole number
leftovers = 12*boxes - cans
totalcost = 14.95*boxes

#output
print(f"We needed {cans} paint cans.")
print(f"We have {leftovers} leftovers ")
print(f"The project costs ${totalcost}")