#   ------- >>> Answer to Programming Exercises <<< ------- #

# 1
collector = 0
for i in range(5):
    bug = input('Please enter the number of bugs collected today: ')
    collector += int(bug)
print('The total number bugs collected is', collector)

# 2
collector_2 = 0
for i in range(10, 31, 5):
    burned_calorie = i*4.2
    print('The number of calories burnt after', i, 'minutes is', burned_calorie, 'calories.')

# 3
fast = 0
slow = 123456789
laps = int(input('Please enter the number of times you ran: '))
lap_time = int(input('Please enter the time it took for lap 1 : '))
fast = lap_time
slow = lap_time
total = 0
for i in range(laps-1):
    i = i + 2
    lap_time = int(input(f'Please enter the time it took for lap {i} : '))
    total = total + lap_time
    if lap_time < fast:
        fast = lap_time
    if lap_time > slow:
        slow = lap_time
average = total / laps
print('The total time for all the laps is', total)
print('The time of the fastest lap is ', fast)
print('The times of the slowest lap is ', slow)
print('Your average lap time is ', format(average, ',.2f'))

# 4
distance = 0
speed = float(input('Please enter the speed of the vehicle: '))
time = int(input('Please enter the number of hours moved by the vehicle: '))
print('Hour  \t Distance Traveled')
for i in range(time):
    i += 1
    distance += i * speed
    print(i, '\t          ', distance)

# 5
years = int(input('Please enter the number of years: '))
rainfall_sum = 0
for i in range(1, years+1):
    for j in range(1, 13, 1):
        rainfall = int(input(f'Please enter rainfall for month {j} year {i}:'))
        rainfall_sum = rainfall_sum + rainfall
months = years * 12
average_rainfall = rainfall_sum/months
print(f'The total number of months is {months}')
print(f'The total inches of rainfall in the months is {rainfall_sum} ')
print(f'The average amount of rainfall in the given months will be {average_rainfall}')

# 6
print('Distance in miles \t Distance in kms')
for i in range(10, 81, 10):
    mile_in_km = 1.60934 * i
    print(i, '       \t          ', format(mile_in_km, ',.2f'))

# 7
days = int(input('Please enter the number of days in the job: '))
initial_salary = 1
total_salary = 0
print('Days \t Salary for the day')
for i in range(days):
    salary = (2**i)/100
    day = i + 1
    total_salary = (total_salary + salary)
    print(day, '  \t   $', salary)
print('The total salary to be received by the end of ')
print('the period will be $', total_salary,)

# 8
counter_1 = 0
counter_2 = 0
average_word = 0
word = input('Please enter a word: ')
while word != '':
    counter_2 += 1
    word = input('Please enter a word: ')
    for i in word:
        counter_1 += 1
    average_word = counter_1 / counter_2
print('The average length of the words entered is', round(average_word))

# 9
print('Years\t Level risen')
for i in range(1, 26, 1):
    height = 1.6 * i
    print(i, '  \t   ', format(height, ',.2f'))

# 10
print('Year \t    Tuition',)
initial_tuition = 8000
print('1   \t  ', format(initial_tuition, ',.2f'))
for i in range(1, 5, 1):
    bonus = initial_tuition * 0.03
    new_tuition = bonus + initial_tuition
    initial_tuition = new_tuition
    print(i+1, '  \t  ', format(initial_tuition, ',.2f'))

# 11
sleep_accumulate = 0
for i in range(1, 8, 1):
    sleep_per_day = int(input(f'Please enter the number of hours for day {i}: '))
    sleep_accumulate = sleep_accumulate + (8 - sleep_per_day)
if sleep_accumulate > 0:
    print('You have a sleep dept of', sleep_accumulate, 'hour.')
else:
    print('What a lucky person you are, I am jealous.')

# 12
number = int(input('Please enter a non-negative number: '))
while number <= 0:
    print('Invalid input')
    number = int(input('Please enter a non-negative number: '))
accumulator = 1
for i in range(number, 1, -1):
    accumulator = accumulator*i
print(f'The factorial of the number is {accumulator}')

# 13
initial_value = int(input('Starting number of organisms: '))
daily_increase = int(input('Average daily increase in percent: '))/100
num_of_days = int(input('Number of days to multiply: '))
print('Day Approximate \t Population')
print('1     \t    ', initial_value)
for i in range(num_of_days-1):
    bonus = initial_value * daily_increase
    new_value = bonus + initial_value
    print(i+2, '   \t    ', format(new_value, ',.2f'))
    initial_value = new_value

# 14
for i in range(7, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')

# 15
for r in range(6):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')

# 16
import turtle
turtle.hideturtle()
turtle.speed(0)
length = 5
turtle.penup()
turtle.goto(40, -50)
turtle.pendown()
for i in range(100):
    turtle.setheading(180)
    turtle.forward(length)
    turtle.setheading(90)
    turtle.forward(length)
    turtle.setheading(0)
    turtle.forward(length)
    turtle.setheading(270)
    turtle.forward(length)
    length += 3

# 17
import turtle
turtle.penup()
turtle.goto(30, 0)
turtle.pendown()
turtle.setheading(180)
for i in range(8):
    turtle.forward(150)
    turtle.right(135)

# 18
import turtle
length_1 = 5
turtle.setheading(90)
turtle.forward(length_1)
for i in range(52):
    turtle.left(90)
    turtle.forward(length_1)
    length_1 += 4

# 19
import turtle
turtle.write('STOP')
turtle.penup()
turtle.hideturtle()
turtle.goto(-35, 120)
turtle.pendown()
for i in range(8):
    turtle.forward(100)
    turtle.right(45)
