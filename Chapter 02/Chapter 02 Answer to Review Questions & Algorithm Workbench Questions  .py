# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,C   6,C   11,A   16,C   21,B
# 2,B   7,A   12,D   17,A   22,B
# 3,D   8,B   13,B   18,B
# 4,B   9,D   14,A   19,A
# 5,A   10,A  15,A   20,B


# ------- >>> Answer to True or False questions <<< ------- #

# 1,F  
# 2,T   
# 3,F   
# 4,T   
# 5,F

# ------- >>> Answer to Short Answer Questions < ------- #

# 1
# To gain an understanding of a problem a programmer must understand what a program
# is supposed to do, usually by interviewing the customer.

# 2
# Pseudocode is written in words that doesn't concern the syntax and are not
# meant to be compiled or executed.

# 3
# Computer program typically perform input receiving, data processing, and displaying output.

# 4
# There are five rules to be considered when naming a variable.
# i, Don't use python's keywords as variable.
# ii, Variable's name can not have spaces within them.
# iii, First character must be small or capital letters and underscore.
# iv, Uppercase and Lowercase are distinct.
# v, You can use numbers after starting with letter and an underscore.

# 5
# Floating point division gives result as floating point number.(in decimals)
# while integer division gives the result as an integer(in whole numbers)

# 6
# Magic number is a number that is unexplained in a programmers code.
# they are problematic because their purpose is not specified, and are
# very hard to correct if a mistake is found.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #


# 1 
# TIP -> the input function always receives and stores data as a string.
age_number = input('Please enter your age here : ')  # Receives age of the user
age = int(age_number)                               # Changing the data type into integer(int)

# 2
color = input('Please enter the name of your favourite color here: ')

# 3
# a -> b = a+2
# b -> a = b*4
# c -> b = a/3.14
# d -> a = b-8

# 4
# a -> x+y = 4+8 = 12
# b -> z*2 = 2*2 = 4
# c -> y/x = 8/4 = 2.0
# d -> y-z = 8-2 = 6
# e -> w//z = 5//2 = 1

# 5
product = 15 * 10

# 6
due = total - down_payment

# 7 
total = subtotal * 0.15

# 8
# according to precedence of the operations b*c will be executed first, and it's result
# 6 will be added to 5 to give the result "11"

# 9
# In the second line of code num will have a new value of 5 so the code will display 
# the number "5"

# 10
sales = 342.398       # This is a sample value for sales
new_sales = format(sales, '.2f')

# 11
number = 1234567.456
number = format(number, ',.1f')    # This code reassigns the value of  the variable number
print(number)

# 12
# The provided code in the question will display the following output
# X       O       X
# O       X       O
# X       O       X

# 13
import turtle
turtle.circle(75)

# 14 
import turtle
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.setheading(270)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.end_fill()

# 15
# to include a circle of 80 pixels inside a 100 pixel length square we need a square of 
# size that is more than diameter of the circle(i,e 160 pixels) or it is going to be the
# square that will be included with in the circle. 
import turtle
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 0)
turtle.forward(50)
turtle.pendown()
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(270)
turtle.forward(50)
