# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,C   6,D   11,D   16,D
# 2,A   7,B   12,B   17,D
# 3,D   8,C   13,B   18,B
# 4,B   9,A   14,B   19,C
# 5,A   10,B  15,A   20,C

# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,True   11,True
# 2,True    7,False  12,False
# 3,False   8,False  13,True
# 4,False   9,True   14,True
# 5,False   10,False 15,True

# ------- >>> Answer to Short answer questions < ------- #

# 1
# Functions help facilitate teamwork by dividing a program into
# specific set of functions that will be programmed by each team
# member for later combination to make the full program.

# 2
# The two parts of the function definition are the header and function's
# block. function's header contains the def keyword and name of the function.
# function's block contains group of statement that specify the functions task.

# 3
# After a function is executed, and the end of the function's block is
# reached the interpreter jumps back to the part of the program that called the function.

# 4
# A local variable is a type of variable that is only accessed by its own function.
# the statements that are able to access a local variable are the block of statements
# that are within the function the local variable exists in.

# 5
# parameter variable have scope that works only inside the function.
# same as local variables. 

# 6
# Out of the many reasons that global variable make debugging difficult,
# one is functions that use global variables are most of the time dependent
# on those variables if one wants to use the same function in a different
# program we will be forced to redesign the function again which is not time effective.

# 7
# I would choose the library function randrange with the following code.
import random
number = random.randrange(0, 30, 5)

# 8
# In a value returning function we must have the statement return.

# 9
#____________________________________________________________
#|______Input_______|_______Process________|____Output_______|
#| Data is accepted | Convert data into    | Data is returned|
#|  from a user.    | string by removing   | to the user as  |
#|                  | the trailing new line| a string.       |
#|__________________|______________________|_________________|

# 10
# Boolean function is a type of function that return either True or False.

# 11
# Breaking large  tasks into many modules is advantageous because the modules
# can be used in more programs as the tasks of the program becomes larger.

# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
def shout(string_1):
    string_1 = string_1.upper()
    print(string_1+'!')

# 2
# show_value(12)

# 3
# a will have the value of 3
# b will have the value of 2
# c will have the value of 1

# 4
def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)


def change_us(a, b):
    a = 0
    b = 0
    print(a, b)


main()
# First the program will display initial values of x and y ( from line 89)
# 1 3.4
# Then the program will display x and y with values of both 0 (from line 90)
# 0 0
# At last the program will display the initial values of x and y (from line 91)
# 1 3.4

# 5
# a) The statement that calls the function and use the specified keyword argument is
print(my_function('testing', 2))
# b) When the function call executes the string values at the 2nd index will be printed
# more about indexes on later chapters

# 6
import random
rand = random.randint(1, 100)

# 7
def half(number):
    number /= 2
    return number

# 8
def cube(num):
    return num * num * num

result = cube(4)

# 9
def times_ten(number):
    return number*10

# 10
def is_valid_length(string_2, length):
    accumulator = 0
    for i in string_2:
        accumulator += 1
    if length > accumulator:
        flag = False
    else:
        flag = True
    return flag
