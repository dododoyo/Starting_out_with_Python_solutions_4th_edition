# ------- >>> Answer to Checkpoints <<< ------- #

# 1
name = 'sample string'
for i in name:
    print(i)

# 2
# The first character in a string have an index 0.

# 3
# TIP- the index of the last character in python is length of string - 1. 

# 4
# An IndexError exception will occur.

# 5
# You can find the length of a string using the len() function.
# Or using loops to count the number of characters.

# 6
animal = 'Tiger'
animal[0] = 'L'
# This code tries to modify a string but because string is immutable
# the interpreter will show a typeerror

# 7
mystring = 'abcdefg'
print(mystring[2:5])
# The code will display the following output.
# cde

# 8
mystring = 'abcdefg'
print(mystring[3:])
# The code will display the following output.
# defg

# 9
mystring = 'abcdefg'
print(mystring[:3])
# The code will display the following output.
# abc

# 10
mystring = 'abcdefg'
print(mystring[:])
# The code will display the following output.
# abcdefg

# 11
if 'd' in mystring:
    print(' d is in mystring. ')
else:
    print('d is not in mystring. ')

# 12
little = big.lower()

# 13
flag = False
for i in ch:
    if i.isdigit():
        flag = True
    else:
        flag = False
if flag:
    print('Digit')
else:
    print('No digit')

# 14
ch = 'a'
ch2 = ch.upper()
print(ch, ch2)
# The following code will display
# a A

# 15
response = 'r'
while response == 'r':
    response = input('Do you want to repeat the program or quit? (R/Q): ')
    response = response.lower()

# 16
var = '$'
print(var.upper())
# The following code will display
# $

# 17
counter = 0
for i in mystring:
    if i.isupper():
        counter += 1

# 18
new_list = days.split()
print(new_list)

# 19
values = 'one$two$three$four'
new_list = values.split('$')
print(new_list)
