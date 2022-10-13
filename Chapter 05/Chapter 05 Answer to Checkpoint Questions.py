# 1
# A function is a set of statements that performs only a specific task.

# 2
# Divide and conquer is a technique used for doing a specific task by
# breaking it down into smaller sub-tasks that will easily be performed.

# 3
# Since the function will be written only once it can be reused by executing
# it in several places when need again and again.

# 4
# If we have a set of programs that will do certain same tasks we can define
# a specific function for the specific task and share the function with other
# developers instead of each developer making a program for the same task.

# 5
# The same answer for question 4 works here too, when a program has a set of
# different tasks to do we can divide the tasks into different parts and
# so that no one is working on the whole program but everyone is working
# on the whole program which is easier and time effective.

# 6
# Functions has two parts, the first is function's header which has key word def
# followed by name of the function. the second part is the functions block
# which is a set of statements belonging to the functions.

# 7
# Since defining a function only specifies what a function does to execute a
# function we must call it. calling a function means executing the function to
# run the block of code.

# 8
# After the end of the function is reached the interpreter jumps back to the program
# that called the functions and the program runs and resumes execution where it left
# this is what is called a function returning.

# 9
# We must indent statements of the block to show that it belongs to the function defined

# 10
# Local variable is a type of variable that exists inside a function and only used by it.

# 11
# Variable's scope is part of the program where a certain variable can be accessed.

# 12
# Yes it is possible for a local variable of certain function to have the same name
# as another function within that program because functions can't access each other's variable.

# 13
# Any piece of data that is passed into a function is called an argument.

# 14
# A type of variable that receive data is called a parameter.

# 15
# Parameter's scope is only inside the function it exists in.

# 16
# No change made to the parameter variable will affect the argument.

# 17
# code (a) passes keyword arguments
# code (b) passes arguments by position

# 18
# A global variable is accessible to all the functions inside a program.

# 19
# A global variable makes debugging difficult. This is because any statement
# in the program can change the value of the global variable if this is done many times
# we will not be able to know if some mistake is made somewhere within the program to fix it.

# 20
# A global constant is a global name that references a value that can't be changed
# throughout the program. Yes it is permissible to use global constants because it
# makes our code less redundant.

# 21
# Value returning functions returns a value back to part of the program that called
# it while void functions only execute the block of statements inside it.

# 22
# Library functions are functions that are pre-written within the programming language.

# 23
# Library functions are called a 'Black Box' because we don't get to see the inner working
# of their internal structure they just receive input and return the output.

# 24
# The statement in checkpoint 5.24 generate some random integer between 1 through 100
# and return that value to the variable x.

# 25
# The statement in checkpoint 5.25 generate some random integer between 1 through 20
# and print the value.

# 26
# The statement in checkpoint 5.26 generate some random integer between 10 through 20
# and print the value.

# 27
# The statement in checkpoint 5.27 generate some random float between 0 through 1
# and print the value.

# 28
# The statement in checkpoint 5.28 generate some random float between 0.1 through 0.5
# and print the value.

# 29
# The seed value is used in the calculation of the next random number in the series.

# 30
# Random numbers generated by random function are called pseudorandom number
# which means they are not truly random, they are calculated using  a seed value
# so, if the same seed value is used the random number will always have the same value.

# 31
# The purpose of the return statements is to return the value of the expression that
# follows the key word return to the program that called the function.

# 32
# a) The name of the function is do_something
# b) The function accepts the argument and return it's doubled value
# c) The statement will return the integer value 20.

# 33
# Boolean functions are type of functions that return a value of either True or False.

# 34
import math
# this is the statement needed to use the maths module.

# 35
import math
square_root = math.sqrt(100)

# 36
import math
degree_to_radian = math.radians(45)
