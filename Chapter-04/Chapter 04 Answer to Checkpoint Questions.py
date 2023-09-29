# ------- >>> Answer to Checkpoint Questions < ------- #

# 1
# Repetition structure is structure that causes statements to execute repeatedly based on some condition.

# 2
# Condition controlled loop uses a True or False condition to control number of times it repeats.

# 3
# Count controlled loop repeats a statement only for the specified amount of times.

# 4
# Iteration is an execution of a body of the loop.

# 5
# While loop is a pretest loop (it tests the condition before performing an iteration.)

# 6
# Hello world will never be displayed because the test will be False in the first iteration
# and the while loop will exit in the first iteration.

# 7
# An infinite loop is a loop that will repeat forever if the program is not interrupted.

# 8
# Rewriting the code with the range function will give
for i in range(6):
    print('I love to program! ')

# 9
for number in range(6):
    print(number)
# The following code will display.
0
1
2
3
4
5

# 10
for number in range(2, 6):
    print(number)
# The following code will display.
2
3
4
5

# 11
for number in range(0, 501, 100):
    print(number)
# The following code will display.
100
200
300
400
500

# 12
for number in range(10, 5, -1):
    print(number)
# The following code will display.
10
9
8
7
6

# 13
# Accumulator is a type of variable that is used to accumulate the total of given numbers.

# 14
# Yes, an accumulator should be specified to a specified to a specific value sot we could get
# the desired outcome(correct sum) of our operation.

# 15
total = 0
for count in range(1, 6):
    total = total + count
print(total)
# The following code will display.
15

# 16
number1 = 10
number2 = 5
number1 = number1 + number2
print(number1)
print(number2)
15
5

# 17
# a) quantity += 1
# b) days_left -= 5
# c) price *= 10
# d) price /= 3

# 18
# Sentinel is a specific value that will mark the end of a sequence use for terminating loop executions.

# 19
# Sentinel must be chosen to be a distinctive value because it must not be mistaken with a regular
# value that will be used in the loop.

# 20
# Garbage In Garbage Out means whatever a computer receives as a data it will process,
# a computer can't tell the difference between bad data and good data.

# 21
# Input validation process is process of clearing out bad data from a program, usually done
# with a loop that iterates as long as the input is bad data.

# 22
# In the input validation process an input is received first and the loop is executed if the data
# is bad, or it will exit if the data is good.

# 23
# Priming read is a process of reading an input before the input validation loop is executed. It's
# purpose is to get the first value that will be tested by the validation loop.

# 24
# The input validation loop will not iterate if the priming read is valid.

