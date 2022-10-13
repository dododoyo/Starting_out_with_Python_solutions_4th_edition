#   ------- >>> Answer to Programming Exercises <<< ------- #

# 1
print('Dolphin Mulugeta')
print('Adama, Ethiopia')
print('+2519--------')
print('Electrical and Computer Engineering.')

# 2
sales_total = int(input('Please enter the projected amount of total sales : '))
profit = sales_total * 0.23
print(format(profit, ',.2f'))

# 3 
mass_in_pounds = int(input('Please enter mass in Pounds: '))
mass_in_kg = mass_in_pounds*0.454
print('Mass of object will be', mass_in_kg, 'Kilograms')

# 4
item_1 = int(input('Please enter the price of the 1st item: '))
item_2 = int(input('Please enter the price of the 2nd item: '))
item_3 = int(input('Please enter the price of the 3rd item: '))
item_4 = int(input('Please enter the price of the 4th item: '))
item_5 = int(input('Please enter the price of the 6th item: '))
sub_total = item_1 + item_2 + item_3 + item_4 + item_5
tax = sub_total*0.07
total = sub_total + tax
print('Subtotal of the purchase is', sub_total)
print('Tax from the total purchase is', tax)
print('Total value of the items is', total)

# 5
speed = 70
distance_1 = 70*6     # This is the distance traveled in 6 hours
distance_2 = 70*10    # This is the distance traveled in 10 hours
distance_3 = 70*15    # This is the distance traveled in 15 hours
print('Distance travelled in 6 hours is', distance_1)
print('Distance travelled in 10 hours is', distance_2)
print('Distance travelled in 15 hours is', distance_3)

# 6


# 7
miles = int(input('Please enter the amount of miles moved: '))
gallons = int(input('Please enter the amount of gallons used: '))
MPG = miles/gallons
print('The car has MPG value of', MPG)

# 8
charge = int(input('Please enter amount of money charged for the food: '))
tip = charge*0.18
tax = charge*0.07
total = tip + tax + charge
print('Total Tip from services provided will be', tip)
print('Total Tax from the services provided will be', tax)
print('Total Charge of services provided will be', total)

# 9
PI = 3.14159
radius = int(input('Please enter the Radius of the circle: '))
area = (radius**2)*PI  # we can also use PI*PI*radius
circumference = radius*2*PI
print('The Circumference of the circle will be', circumference)
print('The Area of the circle will be', area)

# 10
sugar_per_cookies = 1.5/48
butter_per_cookies = 1/48
flour_per_cookies = 2.75/48
cookies_needed = int(input('Please enter the amount of cookies desired: '))
sugar = sugar_per_cookies*cookies_needed
butter = butter_per_cookies*cookies_needed
flour = flour_per_cookies*cookies_needed
print('The amount of sugar needed will be: ', sugar, 'cups')
print('The amount of butter needed will be: ', butter, 'cups')
print('The amount of flour needed will be: ', flour, 'cups')

# 11
males = int(input('Please enter the number of males registered in the class: '))
females = int(input('Please enter the number of females registered in the class: '))
total = males + females
male_percent = (males/total)*100
female_percent = (females/total)*100
print('From the presented data', male_percent, 'percent are males')
print('and', female_percent, 'percent are females. ')

# 12
shares_purchased = 2000
buying_price = 40
selling_price = 42.75
share_purchased_value = buying_price*shares_purchased
share_sold_value = selling_price*shares_purchased
purchase_commission = share_purchased_value*0.03
sold_commission = share_sold_value*0.03
total_purchase = share_purchased_value + purchase_commission  # commission added because it is an extra fee.
total_income = share_sold_value - sold_commission  # commission subtracted because it will be paid from the income
profit = total_income - total_purchase
print('The amount of money Joe paid for the stock is', share_purchased_value)
print('The amount of commission Joe paid when buying the stock is ', purchase_commission)
print('The amount for which joe sold the stock is', share_sold_value)
print('The amount of commission Joe paid when selling the stock is ', sold_commission)
print('Joe made a profit of', profit)

# 13
R = int(input('Please enter length of the row in feet: '))
E = int(input('Please enter amount of space used by and end-post assembly in feet: '))
S = int(input('Please enter the amount of space between vines: '))
V = (R-(2*E))/S
print('The number of grapevines that will fit in a row is', int(V))  # integer value is
# used because grapes are of discrete value. 

# 14
P = float(input('Please enter the amount of money originally deposited: '))
r = float(input('Please enter the annual interest rate in percent: '))/100
t = int(input('Please enter the number of years account will last:  '))
n = float(input('Please enter the number of times per year the interest is compounded: '))
new_time = n*t
new_rate = r/n
A = P*((1+new_rate)**new_time)
print('The amount of money that will exist after', t, 'years is', A)

# 15
# Design 1 (two diamonds close together. )
import turtle
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(225)
turtle.forward(50)
turtle.setheading(315)
turtle.forward(50)
turtle.setheading(45)
turtle.forward(100)
turtle.setheading(315)
turtle.forward(50)
turtle.setheading(225)
turtle.forward(50)
turtle.setheading(135)
turtle.forward(50)
turtle.done()
# Design 2 Two triangles smaller one inside the bigger one
import turtle 
turtle.begin_fill()
turtle.goto(80, 240)
turtle.goto(160, 0)
turtle.goto(80, 120)
turtle.goto(0, 0)
turtle.end_fill()
turtle.goto(160, 0)
# Design 3 Distorted Box
import turtle
turtle.goto(80, 0)
turtle.goto(80, -40)
turtle.goto(40, -40)
turtle.goto(40, 40)
turtle.goto(0, 40)
turtle.goto(0, 0)
turtle.penup()
turtle.goto(0, 40)
turtle.pendown()
turtle.goto(80, -40)
turtle.penup()
turtle.goto(80, 0)
turtle.pendown()
turtle.goto(40, 40)
turtle.penup()
turtle.goto(40, -40)
turtle.pendown()
turtle.goto(0, 0)

# Design 4 Olympics sign
import turtle
turtle.goto(0, 0)
turtle.circle(40)
turtle.penup()
turtle.goto(50, -40)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(150, -40)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.circle(40)

# Design 5
import turtle
turtle.circle(20)
turtle.goto(0, 80)
turtle.penup()
turtle.goto(-8, 80)
turtle.pendown()
turtle.write('North')
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.goto(-60, 20)
turtle.penup()
turtle.goto(-86, 14)
turtle.pendown()
turtle.write('West')
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.goto(60, 20)
turtle.penup()
turtle.goto(64, 14)
turtle.pendown()
turtle.write('East')
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.goto(0, -40)
turtle.penup()
turtle.goto(-8, -50)
turtle.pendown()
turtle.write('South')

# Design 6
import turtle
turtle.goto(90, 90)
turtle.dot()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(-90, -90)
turtle.dot()
turtle.goto(-90, 90)
turtle.goto(-70, 90)
turtle.penup()
turtle.goto(-50, 90)
turtle.pendown()
turtle.goto(-10, 90)
turtle.penup()
turtle.goto(10, 90)
turtle.pendown()
turtle.goto(50, 90)
turtle.penup()
turtle.goto(70, 90)
turtle.pendown()
turtle.goto(90, 90)
turtle.dot()
turtle.goto(90, -90)
turtle.dot()
turtle.goto(70, -90)
turtle.penup()
turtle.goto(50, -90)
turtle.pendown()
turtle.goto(10, -90)
turtle.penup()
turtle.goto(-10, -90)
turtle.pendown()
turtle.goto(-50, -90)
turtle.penup()
turtle.goto(-70, -90)
turtle.pendown()
turtle.goto(-90, -90)
turtle.dot()
turtle.penup()
turtle.goto(-90, 90)
turtle.pendown()
turtle.dot()
turtle.goto(0, 0)
turtle.dot()
turtle.goto(90, -90)
