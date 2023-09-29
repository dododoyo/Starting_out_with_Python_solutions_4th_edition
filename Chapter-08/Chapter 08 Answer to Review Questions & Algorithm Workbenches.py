# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,C   6,C
# 2,D   7,D
# 3,B   8,A
# 4,C   9,B
# 5,A   10,B


# ------- >>> Answer to True or False questions <<< ------- #

# 1,True
# 2,True
# 3,False
# 4,True
# 5,False


# ------- >>> Answer to Short answer questions < ------- #

# 1
mystr = 'abc'
mystr2 = '123'
mystr += mystr2
print(mystr)
# This code will display the following output.
# abc123

# 2
mystr = 'abc' * 3
print(mystr)
# This code will display the following output.
# abcabcabc

# 3
mystr = 'abracadabra'
print(mystr[6:9])
# This code will display the following output.
# dab

# 4
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[4:6])
# This code will display the following output.
# [5, 6]

# 5
name = 'joe'
print(name.lower())
print(name.upper())
print(name)
# This code will display the following output.
# joe
# JOE
# joe

# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
if choice.upper() == 'Y':
    print('you choose y')
# or you can use
if choice.lower() == 'y':
    print('you choose y')

# 2
counter = 0
for i in mystring:
    if i == ' ':
        counter += 1

# 3
counter = 0
for i in mystring:
    if i.isalnum():
        counter += 1

# 4
counter = 0
for i in mystring:
    if i.islower():
        counter += 1

# 5
def have_https(some_string):
    flag = False
    if some_string.startswith('https'):
        flag = True
    else:
        flag = False
    return flag

# 6
# Instead I wrote a function.
def T_converter(some_string):
    new_string = ''
    for i in some_string:
        if i.lower() == 't':
            new_string += i.upper()
        else:
            new_string += i
    some_string = new_string
    return some_string

# 7
def return_backward(string_2):
    new_string = ''
    length = len(string_2)
    j = length - 1
    while j >= 0:
        new_string += string_2[j]
        j -= 1
    return new_string

# 8
sliced_mystring = mystring[:3]
print(sliced_mystring)

# 9
sliced_mystring = mystring[-3:]
print(sliced_mystring)

# 10
levels = 'Beginner, Average, Advanced, Expert'
new_list = levels.split()
print(new_list)
