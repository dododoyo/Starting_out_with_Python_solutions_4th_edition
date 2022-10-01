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
