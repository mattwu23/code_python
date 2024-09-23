#input
start = int(input("What was the starting amount? "))
num_cookies = input("How many normal cookies did you sell? ")
num_big = input("How many big cookies did you sell? ")

#processing
normal = len(num_cookies)
big = len(num_big)
total = normal + big

cost = (big*.75) + (normal*.5)
sales = (big*2) + (normal*1.25)

profit = sales-cost

end = start + profit 

#output
print(f"There were {total} cookies sold")
print(f"You made {profit} in profit")
print(f"Your final balance is {end}")