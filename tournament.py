#takes wins/loss input from user and places them in groups
win_counter = 0
for i in range(6):
    current_result = input(f"Enter game {i+1} result (W/L): ")

    if current_result=='W':
        win_counter += 1

group = 0

if win_counter>4:
    group = 1
elif win_counter>2:
    group = 2
elif win_counter>0:
    group = 3

if group==0:
    print("You have been eliminated")
else:
    print(f"You are in group {group}")
