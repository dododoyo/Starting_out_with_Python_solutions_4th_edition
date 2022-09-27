people = int(input('Please enter the number of people attending: '))
hotdog_per_people = int(input('Please enter hot dog provided for each person: '))
total_hotdog = people*hotdog_per_people
bun = total_hotdog//8
added_bun = total_hotdog%8
left_bun = 8 - added_bun
hotdog = total_hotdog//10
added_hotdog = total_hotdog%10
left_hotdog = 10 - added_hotdog
if added_bun == 0:
    bun = bun
else:
    bun = bun + 1
if added_hotdog == 0:
    hotdog = hotdog
else:
    hotdog = hotdog +1
print('The minimum number of packages of hot dogs required is',hotdog)
print('The minimum number of packages of hot dog buns required is',bun)
print('The number of hot dogs that will be left over is',left_hotdog)
print('The number of hot dog buns that will be left over is',left_bun)