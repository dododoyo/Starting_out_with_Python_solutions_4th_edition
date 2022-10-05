# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   6,B   11,D
# 2,D   7,D   12,A
# 3,D   8,A
# 4,A   9,B
# 5,C  10,C


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,False
# 2,True    7,False
# 3,True
# 4,False
# 5,True


# ------- >>> Answer to Short answer questions < ------- #

# 1
# Condition-controlled loop is a loop that iterates only if the condition of the loop
# is met.( is True)

# 2
# Count-controlled loop is a loop that iterates only for the specified amount of items.

# 3
# An infinite loop is a loop that terminates only if the program is stopped, and goes on forever if not.

# 4
# An accumulator can be viewed as a cart for the user as he goes on in a super-market. He adds the items in
# the cart, it is the same case with an accumulator as the loop iterates it adds the iterated item to the
# accumulator and at the end of the iteration the accumulator will have the total value.

# 5
# 4 x 5 = 20

# 6
# Because not to confuse its value with value to be operated by the loop sentinel must be carefully selected.

# 7
# It means bad data entered as input will result bad output computer doesn't have the idea of bad or good data
# it will execute on whatever is entered.

# 8
# An input validation process is a process used to get rid of bad data by "trapping" the user inside a while loop
# until the user enters the proper data.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
number = int(input('Please enter the number: '))
while number < 100:
    product = number * 10

# 2
snt = 'y'
while snt == 'y' or snt == 'Y':
    number_1 = int(input('Please enter the first number.: '))
    number_2 = int(input('Please enter the second number: '))
    print(number_2+number_1)
    snt = input('Please enter y if you wish to continue')

# 3
for i in range(1, 100, 2):
    print(i)

# 4
text = ''
length = 0
while length < 10:
    new_in = input('Please enter the word: ')
    for i in new_in:
        length += 1
    text = text + new_in
    print(text)

# 5
j = 30
counter = 0
for i in range(1, 31, 1):
    num_1 = i/j
    counter += num_1
    j -= 1
print(counter)

# 6
# a, x += 1
# b, x *= 2
# c, x /= 10
# d, x -= 100

# 7
for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        product = j * i
        print(i, 'x', j, '=', product)
    print('')

# 8
num_2 = int(input('Please enter a positive non-zero number: '))
while num_2 <= 0:
    print('Invalid value. ')
    num_2 = int(input('Please enter a positive  non-zero number again: '))
print('Thank you, you have entered the correct value.')

# 9
num_3 = int(input('Please enter a number within range of 1 through 100. '))
while num_3 <= 1 and num_3 >= 100 :
    print('Invalid value. ')
    num_3 = int(input('Please enter a positive  non-zero number again: '))
print('Thank you, your number is valid.')
