minutes = int(input())
total_chores = int(input())
duration = []
for i in range (total_chores):
    time = int(input())
    if time <= minutes: 
        duration.append(time)
    
duration.sort()
counter = 0

while time>0:
    
    if duration[i] >time:
        break
    else:
        time-=duration[i]
        counter+=1
        i+=1

print(counter)
    
