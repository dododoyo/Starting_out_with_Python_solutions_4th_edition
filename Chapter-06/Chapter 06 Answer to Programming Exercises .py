#   ------- >>> Answer to Programming Exercises <<< ------- #
# 1
numbers = open('numbers.txt', 'r')
for line in numbers:
    print(line)
numbers.close()

# 2
file_name = input('Please enter the file name:  ')
counter = 0
counter2 = 1
new_file = open(file_name, 'r')
for lines in new_file:
    counter += 1
new_file = open(file_name, 'r')
if counter <= 5:
    for lines in new_file:
        print(lines)
else:
    new_line = new_file.readline()
    while counter2 <= 5:
        print(new_line)
        new_line = new_file.readline()
        counter2 += 1
new_file.close()

# 3
name_file = input('Please enter the file name:  ')
temp_file = open(name_file, 'r')
counter3 = 0
counter4 = 1
for line in temp_file:
    counter3 += 1
temp_file = open(name_file, 'r')
temp_line = temp_file.readline()
while temp_line != '':
    print(counter4, ':', temp_line)
    temp_line = temp_file.readline()
    counter4 += 1
temp_file.close()

# 4
new_file = open('scores.txt', 'r')
highest = 0
the_man = ''
counter = 0
name = new_file.readline()
score = new_file.readline()
while name != '':
    if int(score) > highest:
        highest = int(score)
        the_man = name.rstrip('\n')
    counter += 1
    name = new_file.readline()
    score = new_file.readline()
print(the_man)
print(highest)
print(counter)
new_file.close()

# 5
counter = 0
numbers = open('numbers.txt', 'r')
for line in numbers:
    counter += int(line)
numbers.close()

# 6
counter1 = 0
counter2 = 0
numbers = open('numbers.txt', 'r')
for line in numbers:
    counter1 += 1
numbers = open('numbers.txt', 'r')
for line in numbers:
    counter2 += int(line)
average = counter2/counter1
print('Average value will be: ', average)
numbers.close()

# 7
op_file = open('wordlist.txt', 'w')
num_of_time = int(input('How many files would you like to add? : '))
for i in range(num_of_time):
    files = input('Please enter data ' + str(i+1) + ': ')
    op_file.write(files + '\n')
op_file.close()
print('That will be all for today. \n Thank you ')
op_file.close()

# 8


def _len_(string1):
    cntr4 = 0
    for k in string1:
        cntr4 += 1
    return cntr4  # We can also use python's builtin len() function


cntr2 = 0
cntr3 = 0
file_op = open('wordlist.txt', 'r')
for line in file_op:
    cntr2 += 1  # counts number of data in file

file_op = open('wordlist.txt', 'r')
max_ = _len_(file_op.readline())
for line in file_op:
    if _len_(line) > max_:  # gets the maximum letters in a given word
        max_ = _len_(line)
    cntr3 += _len_(line)  # counts the number of letters in the word and adds it
file_op = open('wordlist.txt', 'r')
read_line = file_op.readline()
long_est = ''
while read_line != '':
    if max_ == _len_(read_line):
        long_est = read_line  # get the longest word
    read_line = file_op.readline()

average = cntr3 / cntr2
print('There are ' + str(cntr2) + ' number of lines.')
print('Average value of letters per word is' + str(average))
print('The longest word is: ' + long_est)
file_op.close()

# 9
try:
    counter1 = 0
    counter2 = 0
    numbers = open('numbers.txt', 'r')
    for line in numbers:
        counter1 += 1
    numbers = open('numbers.txt', 'r')
    for line in numbers:
        counter2 += int(line)
    average = counter2 / counter1
    print('Average value will be: ', average)
    numbers.close()
except IOError:
    print('An error occurred trying to read the file.')
except ValueError:
    print('Non-numeric data found in the file. ')
numbers.close()
# 10
# Data Collector
data_store = open('golf.txt', 'w')


def data_collector():
    data1 = input('Please enter the name of the player: ')
    data2 = input('Please enter the score of the player: ')
    data_store.write(data1 + '\n')
    data_store.write(data2 + '\n')


data_collector()
while True:
    answer = input('Would you like to add another data? "y" or "n":  ')
    if answer == 'y':
        data_collector()
    else:
        print(' \n Thank you, That will be all for today. ')
        break
data_store.close()

# Data Viewer
data_store = open('golf.txt', 'r')
name = data_store.readline()
score = data_store.readline()
name = name.rstrip('\n')
counter5 = 1
while name != '':
    print('Player ' + str(counter5) + ': ' + name)
    print('Score: ' + score)
    counter5 += 1
    name = data_store.readline()
    score = data_store.readline()
    name = name.rstrip('\n')
data_store.close()

# 11
portfolio = open('portfolio.html', 'w')
name = input('Please enter your name:  ')
description = input("Describe yourself: ")
portfolio.write('<!DOCTYPE html>' + '\n')
portfolio.write('<html lang="en">' + '\n')
portfolio.write('<head>' + '\n')
portfolio.write('</head>' + '\n')
portfolio.write('<body>' + '\n')
portfolio.write('  ' + '<center>' + '\n')
portfolio.write('    ' + '<h1>' + name + '</h1>' + '\n')
portfolio.write('  ' + '</center>' + '\n')
portfolio.write('  ' + '<hr/>' + '\n')
portfolio.write('  ' + description + '\n')
portfolio.write('  ' + '<hr/>' + '\n')
portfolio.write('</body>' + '\n')
portfolio.write('</html>' + '\n')
portfolio.close()

# 12
# if the steps.txt file described in the question isn't accessible to you
# can use the random module to generate steps of the year with in a range
import random
steps = open('steps.txt', 'w')
for i in range(365):
    daily = random.randint(2000, 5000)
    steps.write(str(daily) + '\n')
steps.close()
# remember to code this on another file since python can't read and write a file at the same time.

liner = open('steps.txt', 'r')


def average_(month, month_no):
    ano_cntr = 0
    for x in range(month_no):
        line2 = liner.readline()
        line2 = int(line2)
        ano_cntr += line2
    answer2 = str(ano_cntr/month_no)
    print('Average steps of month ' + month + ' is ' + answer2+'.')


average_('January', 31)
average_('February', 28)
average_('March', 31)
average_('April', 30)
average_('May', 31)
average_('June', 30)
average_('July', 31)
average_('August', 31)
average_('September', 30)
average_('October', 31)
average_('November', 30)
average_('December', 31)
liner.close()
