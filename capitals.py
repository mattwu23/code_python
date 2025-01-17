city = ['Ankara', 'Brasilia', 'Dhaka', 'Lisbon', 'Manila', 'Rome']
country = ['Turkey', 'Brazil', 'Bangladesh', 'Portugal', 'Philippines', 'Italy']

for i in range(0, len(country)-1):
    current = country[i]
    track = i
    for j in range(i+1, len(country)):
        if country[j] < current:
            current = country[j]
            track = j

    
    country[i], country[track] = country[track], country[i]
    city[i], city[track] = city[track], city[i]

print(country)
print(city)