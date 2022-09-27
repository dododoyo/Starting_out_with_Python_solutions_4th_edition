# 1

_int = int(input('Please enter the number: '))
if _int == 0:
    print('Zero')
elif _int > 0:
    print('Positive')
else:
    print('Negative')
if _int%2 == 0: # this line of code tests of remainder of the number when devided by two
                # the remainder is zero shows it is even.
    print('Even')
else:
    print('Odd')

# 2
hieght_1 = float(input('Please enter the hieght of the first rectangle: '))
hieght_2 = float(input('Please enter the hieght of the second rectangle: '))
length_1 = float(input('Please enter the length of the first rectangle: '))
length_2 = float(input('Please enter the length of the second rectangle: '))
area_1 = hieght_1*length_1
area_2 = hieght_2*length_2
if area_1 > area_2:
    print('The first rectangle has the largest Area.')
elif area_2 > area_1:
    print('The second rectangle has the largest Area.')
else:
    print('The rectangles have the same area')

# 3
month = int(input('Please enter the month as a number \n for example january = 1 february = 2 and so on: '))
if month >= 1 and month <=3:
    print('The month is in the first quarter. ')
elif month >= 4 and month <= 6:
    print('The month is in the second quarter. ')
elif month >= 7 and month <= 9:
    print('The month is in the third quarter. ')
elif month >= 10 and month <= 12:
    print('The month is in the fourth quarter. ')
else:
    print('There has been an error in the entered value. ')
    print('PLEASE ENTER VALUES 1 THROUGH 12')

# 4
number_1 = int(input('Please enter a number: '))
if number_1 == 1:
    print('The Roman numeral of the number is')
    print('I')
elif number_1 == 2:
    print('The Roman numeral of the number is')
    print('II')
elif number_1 == 3:
    print('The Roman numeral of the number is')
    print('III')
elif number_1 == 4:
    print('The Roman numeral of the number is')
    print('IV')
elif number_1 == 5:
    print('The Roman numeral of the number is')
    print('V')
elif number_1 == 6:
    print('The Roman numeral of the number is')
    print('VI')
elif number_1 == 7:
    print('The Roman numeral of the number is')
    print('VII')
elif number_1 == 8:
    print('The Roman numeral of the number is')
    print('VIII')
elif number_1 == 9:
    print('The Roman numeral of the number is')
    print('IX')
elif number_1 == 10:
    print('The Roman numeral of the number is')
    print('X')
else:
    print('Please enter values 1 through 10. ')

# 5
mass = float(input('Please enter the mass of the object: '))
wieght = mass*9.8
if wieght>500:
    print('The mass is too heavy. ')
elif wieght<100:
    print('The mass is too light. ')

# 6
_day = int('Please enter the day "in numeric form": ')
_month = int('Please enter the month "in numeric form": ')
_year = int('Please enter the ;ast two digits of the year "in numeric form": ')
if _day*_month == _year:
    print('The date is a magic date. ')
else:
    print('The date is not a magic date. ')

# 7
test_1 = float(input('Please enter your result on Test-1:  '))
test_2 = float(input('Please enter your results on Test-2:  '))
exam = float(input('Please enter your results from the final Exam: '))
total_score = test_1 + test_2 + exam
testresults = test_1 + test_2
if total_score>=50 and testresults>=25:
    if total_score>=80:
        print('Passed with Distniction grade.')
    elif total_score>=60 and total_score<80:
        print('Passed with a Credit grade.')
    elif total_score>=50 and total_score<60:
        print('Passed. ')
else:
    print('Fail. ')

# 8
people = int(input('Please enter the number of people attending: '))
hotdog_per_people = int(input('Please enter hot dog provided for each person: '))
total_hotdog = people*hotdog_per_people
bun = total_hotdog//8           # this code gives us value of integer division
added_bun = total_hotdog%8      # this code gives us number of hotdog bun that will be needed additionally
left_bun = 8 - added_bun
hotdog = total_hotdog//10        # this code gives us value of integer division
added_hotdog = total_hotdog%10   # this code gives us number of hotdog that will be needed additionally
left_hotdog = 10 - added_hotdog
if added_bun == 0:
    bun = bun
    left_bun = 0
else:
    bun = bun + 1
if added_hotdog == 0:
    hotdog = hotdog
    left_hotdog = 0
else:
    hotdog = hotdog +1
print('The minimum number of packages of hot dogs required is',hotdog)
print('The minimum number of packages of hot dog buns required is',bun)
print('The number of hot dogs that will be left over is',left_hotdog)
print('The number of hot dog buns that will be left over is',left_bun)

# 9
pocket_number = int(input('Please enter your pocket number: '))
if pocket_number == 0:
    print('pocket color is green')
elif pocket_number>=1 and pocket_number<=10:
    if pocket_number%2 == 0:
        print('pocket coloris black. ')
    else:
        print('pocket color is red')
elif pocket_number>=11 and pocket_number<=18:
    if pocket_number%2 == 0:
        print('pocket color is red. ')
    else:
        print('pocket color is black')
elif pocket_number>=19 and pocket_number<=28:
    if pocket_number%2 == 0:
        print('pocket color is black. ')
    else:
        print('pocket color is red')
elif pocket_number>=29 and pocket_number<=36:
    if pocket_number%2 == 0:
        print('pocket color is red. ')
    else:
        print('pocket color is black')
else:
    print('Error; You entered an invalid value. ')
    print('Please enter values 0 through 36. ')

# 10
pennies = int(input('Please enter the number of pennies you have: '))*0.01
nickels = int(input('Please enter the number of nickels you have: '))*0.05
dimes = int(input('Please enter the number of dimes you have: '))*0.1
quarters = int(input('Please enter the number of quarters you have: '))*0.25
total_count = nickels + dimes + quarters + pennies
if total_count == 1:
    print('Congratulations, You won the game. ')
elif total_count > 1:
    print('You entered more than a dollar. ')
else:
    print('You entered less than a dollar. ')

# 11
books = int(input('Please enter the number of books purchased: '))
if books==0 or books==1:
    print('You earn 0 points.')
elif books==2 or books==3:
    print('You earn 5 points.')
elif books==4 or books==5:
    print('You earn 15 points.')
elif books==6 or books==7:
    print('You earn 30 points.')
elif  books>=8:
    print('You earn 60 points.')
else:
    print('You have entered an invalid value.')

# 12
packages = int(input('Please enter the number of packages purchased: '))
total_purchase = 99*packages
if packages < 10:
    discount = 0
elif packages >= 10 and  packages <= 19:
    discount = 0.1
elif packages >= 20 and  packages <= 49:
    discount = 0.2
elif packages >= 50 and  packages <= 99:
    discount = 0.3
elif packages >= 100:
    discount = 0.4
else:
    print('Invalid number of purchased quantity.')
total_discount = discount*total_purchase
new_purchase = total_purchase-total_discount
print('Total discount you get from your purchase is',total_discount)
print('Total amount of purchase after discount is',new_purchase)

# 13
__wieght = int(input('Please enter the wieght of your packages: '))
if _wieght <= 2 and _wieght>0:
    charge = _wieght*1.5
    print('The total shipping charges will be', charge)
elif _wieght > 2 and _wieght<=6:
    charge = _wieght*3
    print('The total shipping charges will be', charge)
elif _wieght > 6 and _wieght<=10:
    charge = _wieght*4
    print('The total shipping charges will be', charge)
elif _wieght > 10 :
    charge = _wieght*4.75
    print('The total shipping charges will be', charge)
else:
    print('Invalid amount of package. ')

# 14 
hieght_3 = float(input('Please enter yuor hieght: '))
wieght_2 = float(input('Please enter your wieght: '))
BMI = (wieght_2*703)/(hieght_3**2)
if BMI < 18.5 and BMI >0:
    print('You are underwieght, hit the GYM. ')
elif BMI>=18.5 and BMI<25:
    print('You are in good shape.')
elif BMI>=25:
    print('You are over wieght, hit the GYM. ')
else:
    print('Invalid Value.')

# 15
seconds = int(input('Please enter the number of seconds: '))
if seconds >= 60 and seconds < 3600:
    minutes = seconds//60
    seconds_left = seconds%60
    print('These seconds equal to',minutes,'minutes and',seconds_left,'seconds. ')
elif seconds >= 3600 and seconds < 86400:
    hours = seconds//3600
    minutes = (seconds//60) - (hours*60)
    seconds_left = seconds%60
    print('These seconds equal to',hours,'hours',minutes,'minutes and',seconds_left,'seconds. ')
elif seconds >= 86400:
    days = seconds//86400
    hours = (seconds//3600) - (days*24)
    minutes = (seconds//60)-(hours*60)-(days*24*60)
    seconds_left = seconds%60
    print('These seconds equal to',days,'days,',hours,',hours',minutes,'minutes, and',seconds_left,'seconds. ')
else:
    print('Invalid amount of seconds.')

# 16
year = int(input('Please enter the year: '))
if year%100==0 and year%400 == 0:
    print('In',year,'February has 29 days. ')
elif year%100!= 0 and year%4 == 0:
    print('In',year,'February has 29 days. ')
else:
    print('In',year,'February has 28 days. ')

# 17
print('Reboot the router and try to connect.')
connected = input('Did that fix the problem? ')
if connected == 'no':
    print('Make sure the cables between the router and modem are plugged in firmly. ')
    connected = input('Did that fix the problem? ') 
    if connected == 'no':
         print('Move the router to a new location and try to connect.')
         connected = input('Did that fix the problem? ')
         if connected == 'no':
            print('Get a new router.')

# 18
vegeterian = input('Is anyone in your party vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in you party gluten-free? ')
print('Here are your restaurant choices: ')
if vegeterian== 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
if vegeterian== 'yes' and vegan == 'no' and gluten_free == 'no':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
    print('    Mama\'s Fine Italian')
    print('    Main Street Pizza Company')
if vegeterian== 'yes' and vegan == 'yes' and gluten_free == 'no':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
if vegeterian== 'yes' and vegan == 'no' and gluten_free == 'yes':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
    print('    Main Street Pizza Company')
if vegeterian== 'no' and vegan == 'yes' and gluten_free == 'yes':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
if vegeterian== 'no' and vegan == 'no' and gluten_free == 'no':
    print('Joe\'s Gourment Burgers')
if vegeterian== 'no' and vegan == 'no' and gluten_free == 'yes':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
    print('    Main Street Pizza Company')
if vegeterian== 'no' and vegan == 'yes' and gluten_free == 'no':
    print('    Corner Cafe')
    print("    The Chef's Kitchen")
    
# 19
import turtle  
# Named constants
SCREEN_WIDTH = 600     # Screen width
SCREEN_HEIGHT = 600    # Screen height
TARGET_LLEFT_X = 100   # Target's lower-left X
TARGET_LLEFT_Y = 250   # Target's lower-left Y
TARGET_WIDTH = 25      # Width of the target
FORCE_FACTOR = 30      # Arbitrary force factor
PROJECTILE_SPEED = 1   # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction
# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT) 
# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
turtle.goto(0, 0)    # Center the turtle.
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
  # Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))
distance = force * FORCE_FACTOR    # Calculate the distance.
turtle.setheading(angle)     # Set the heading.
turtle.pendown()       # Launch the projectile.
turtle.forward(distance)
if (turtle.xcor() >= TARGET_LLEFT_X and
      turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
      turtle.ycor() >= TARGET_LLEFT_Y and
      turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Target hit!')
elif force >8.97 and force <10.07 and angle>69:
    print('Target not hit!, please Decrease the angle. ')
elif force >8.97 and force <10.07 and angle<69:
    print('Target not hit!, please Increase the angle. ')
elif angle >63.43 and force <10.07 and angle<69:
    print('Target not hit!, please Increase the force. ')
elif angle >63.43 and force >10.07 and angle<69:
    print('Target not hit!, please Decrease the force. ')
