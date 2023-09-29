# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,C   6,B   11,C  
# 2,B   7,C   12,A   
# 3,D   8,D    
# 4,A   9,A   
# 5,C   10,B  
  

# ------- >>> Answer to True or False questions <<< ------- #

# 1,False 
# 2,True  
# 3,False  
# 4,True  
# 5,False


# ------- >>> Answer to Short Answer Questions < ------- #
# 1 
# The term Conditionally executed is used to specify a type of code
# that is executed only when a certain criteria is met.

# 2 In a single alternative decision structure task is provided only one path to be executed
# while  dual alternative decision structure provides two possible paths for execution.

# 3 
# The and operator is a logical operator that assigns True for a compound boolean expression
# when only both subexpressions are True.

# 4
# The or operator is a logical operator that assigns False value for a compound boolean expression
# when only both subexpressions are False.

# 5 
# It is best to use the and operator

# 6. 
# A Flag is a type of variable that indicates some condition exists with in a program,
#  it works by having value of True when condition is met and value False when condition isn't met.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
if x > 100:
    y = 20
    z = 40

# 2
if a == 100:
    b = 10
    c = 50

# 3
if a < 10:
    b = 0
else:
    b = 99
    
# 4
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

# 5
if amount1 > 10 and amount1 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)
# 6
if score >= 40 and score <= 49:
    again = True
else:
    again = False

# 7
if points < 9 and points > 51:
    print('invalid points.')
else:
    print('valid points.')
# 8
import turtle
turtle_heading = turtle.heading()
if turtle_heading >= 0 and turtle_heading <= 45:
    turtle.penup()

# 9
import turtle
if turtle.pensize() > 1 or turtle.pencolor() == 'red':
    turtle.pensize(1)
    turtle.pencolor('blue')

# 10
x_cord = turtle.xcor()
y_cord = turtle.ycor()
x_range = x_cord > 100 and x_cord < 200
y_range = y_cord > 100 and y_cord < 200

if x_range and y_range:
    turtle.hideturtle()
