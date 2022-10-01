# 1 
# control structure is type of logical design that controls the order of statements execution. 

# 2 
# decision struction is a type of logical design where an active 
# is performed only if certain criterea is met.

# 3 
# single alternative decision structure provides only one alternate path for excution,
# if critera is not met the program will exit.

# 4 
# Boolean expression are expressions tested by an if statement. 
# They can only have a value of either True or False (like statments in mathmatics.) 

# 5 
# equality == . inequality !=, comparson (>,<, >=,<=)

# 6 
if y==20:
    x=0

# 7
if sales >= 10000:
    Commission_Rate = 0.2

# 8 
# dual alternative decision structure works by having two possible 
# paths of excution one path is taken if condition is True 
# and another is the condition is False

# 9 
# we will use if-else statement for a dual alternative decision structure in python.

# 10, 
# the statements under else statement will excute if the condition is false.

# 11 
# the code will display 
# 'z is to not less than a'

# 12
# The code will display 
# Boston
# New york

# TIP nested if conditions are same as the if conditions connected with and.

# 13
if number == 1:
    print ("one")
elif number == 2:
    print ("two")
elif number == 3:
    print ("Three")
else:
    print ("Unknown")

# 14
# Compound boolean expression is an expression where 
# multiple boolean expression are connected with logical operators.

# 15. 
# According to the rules of the operators
#     True and False -> False
#     True and True  -> True
#     False and True -> False
#     False and False-> False
#     True or False  -> True
#     True or True   -> True
#     False or True  -> True
#     False or False -> False
#     not True       -> False
#     not False      -> True

# 16
# with values a=2, b=4, and c=6
# a == 4 (False) or b > 2(True) -> True
# 6 <= c (True) and a > 3(False)-> False
# 1 != b (True) and c != 3(True)-> True
# a >= -1 (True) or a <= b(True)-> True
# not(a>2(True))                -> False

# 17 
# short circuit evaluation is a method that checks only
# the first conditons of compound boolean expression to work
# effectively it assigns False value to expressions if the 
# first boolean is False in the compound operation connect 
# with and operator, and it assigns True value for an expression 
# starting with True value for boolean expression connected with 
# or operator without checking the second condition. 

#18
if speed >=0 and speed <= 200:
    print("The number is valid ")

# 19    
if speed <=0 and speed >=200:
    print(" The number is not valid")

# 20
# The bool variable can only have Values of either the True or False.

# 21 
# Flag is a type of variable that signals when some condition exists in a program.

# 22  
# By using the funtion turtle.xcor() and turtle.ycor()

# 23 
# You can determine whether turtle's pen is up or down by using the
# turtle.isdown() function returning a True value indicates the turtle pen is down.

# 24 
# We can use turtle.heading() function to get turtles current heading in degree.

# 25 
# By using turtle.isvisible() function which means it's visible if 
# function returns value of True,and value is False means turtle is not visible

# 26 
# You can determine turtle's pen color using turtle.pencolor() which returns 
# pen's current drawing color as a string. You can also determine the turtle's 
# fill color by using the turtle.fillcolor() to get turtles fill color as a string.
# at last you can use turtle.bgcolor() to get turtles background color as a string.

# 27 
# Turtle's current pen size can be determined by excuting turtles.pensize() function.

# 28 
# Turtle's current animation speed could be determined by excuting the turtle.speed() function.
