#   ------- >>> Answer to Programming Exercises <<< ------- #
# 1
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
def total_finder(some_list):
    accumulator = 0
    for o in some_list:
        accumulator += o
    return accumulator
for i in numbers:
    if i >= 0 and i <= 100:
        valid_numbers.append(i)
print(f'The total value of the valid numbers is {total_finder(valid_numbers)}.')
print(f'The average value of the valid numbers is ', format(total_finder(valid_numbers)/len(valid_numbers), ',.2f'))

# 2
import random
lottery_numbers = []
for i in range(7):
    n = random.randint(1, 9)
    lottery_numbers.append(n)
for m in lottery_numbers:
    print(m)

# 3
rainfall_of_year = []
total_rainfall = 0  # Or we can use the total finder for the list
for r in range(1, 13, 1):
    r = int(input(f'Please enter the rainfall amount for month {r}: '))
    rainfall_of_year.append(r)
    total_rainfall += r
minimum = min(rainfall_of_year)
maximum = max(rainfall_of_year)
min_index = rainfall_of_year.index(minimum)
max_index = rainfall_of_year.index(maximum)
average = total_rainfall/(len(rainfall_of_year))
print(f'The total rainfall of the year is {total_rainfall}.')
print('The average monthly rainfall of the year is', format(average, ',.2f'))
print(f'The month with the highest rainfall is month {max_index+1} with value of {maximum}.')
print(f'The month with the lowest rainfall is month {min_index+1} with value of {minimum}.')

# 4
number_list = []
total_of_list = 0
for i in range(1, 21):
    i = int(input(f'Please enter number {i}: '))
    number_list.append(i)
the_minimum = min(number_list)
the_maximum = max(number_list)
for i in number_list:
    total_of_list += i
average_of_list = total_of_list/(len(number_list))
print(f'The minimum number from the list is {the_minimum}.')
print(f'The maximum number from the list is {the_maximum}')
print(f'The total of the numbers in the list is {total_of_list}')
print('The average value from the list of values is', format(average_of_list, ',.2f'))

# 5
charge_account = open('charge_accounts.txt', 'r')
lines_list = charge_account.readlines()
charge_account.close()
The_number = int(input('Please enter the charge account number: '))
index = 0
while index < len(lines_list):
    lines_list[index] = lines_list[index].rstrip('\n')
    index += 1
if The_number in lines_list:
    print('The charge account number is valid.')
else:
    print('The charge account number is Invalid.')

# 6
import random
def roll(number_of_throws):
    new_lists = []
    for u in range(number_of_throws):
        u = random.randint(1, 6)
        new_lists.append(i)
    return new_lists
throws = int(input('Please enter the number of throws: '))
print(roll(throws))

# 7
correct_answer = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A',  'D', 'C', 'B', 'B', 'D', 'A']
student_answer_txt = open('student_answer.txt', 'r')
student_answer_list = student_answer_txt.readlines()
student_answer = []
i = 0
while i < len(student_answer_list):
    student_answer_list[i] = student_answer_list[i].rstrip('\n')
    i += 1
student_answer_txt.close()
right_answers = 0
indeces = []
index = 0
while index < len(student_answer_list):
    if student_answer_list[index] == correct_answer[index]:
        right_answers += 1
    else:
        indeces.append(index)
    index += 1
if right_answers >= 15:
    print(f'The student PASSED the exam with a score {right_answers} / 20.')
else:
    print(f'The student did not PASS the exam having a score {right_answers} / 20')
    print('Here is a list of question numbers the student got wrong. ')
    print(indeces)

# 8
girls_txt = open('GirlNames.txt', 'r')
boys_txt = open('BoyNames.txt', 'r')
girls_list = girls_txt.readlines()
boys_list = boys_txt.readlines()
boys_txt.close()
girls_txt.close()
i = 0
while i < len(boys_list):
    boys_list[i] = boys_list[i].rstrip('\n')
    girls_list[i] = girls_list[i].rstrip('\n')
    i += 1
boy_name = input("Please enter the boy's name. or hit 'enter' to skip: ")
girl_name = input("Please enter the girl's name. or hit 'enter' to skip: ")
if boy_name == '':
    if girl_name in girls_list:
        print('The name is among the 200 most popular names.')
if girl_name in girls_list and boy_name in boys_list:
    print('Both the names are among the 200 most popular names.')
if girl_name not in girls_list and boy_name in boys_list:
    print("The boy's name among the 200 most popular names.")
if girl_name in girls_list and boy_name not in boys_list:
    print("The girl's name among the 200 most popular names.")

# 9
population_txt = open('USPopulation.txt', 'r')
population_list = population_txt.readlines()
population_txt.close()
i = 0
while i < len(population_list):
    population_list[i] = population_list[i].rstrip('\n')
    i += 1
total_change = []
j = 0
while j > 49:
    num1 = int(population_list[j])
    num2 = int(population_list[j + 1])
    difference = num2 - num1
    total_change.append(difference)
    j += 1
minimum_change = min(total_change)
maximum_change = max(total_change)
total_change_summed = 0
for i in total_change:
    total_change_summed += i

average = total_change_summed / len(total_change)
print('The average annual change in population will be', format(average, ',.2f'))
print(f'The year with the greatest change in population is {maximum_change}')
print(f'The year with the smallest change in population is {minimum_change}')

# 10
world_win_txt = open('WorldSeriesWinners.txt', 'r')
world_list = world_win_txt.readlines()
world_win_txt.close()
i = 0
while i < len(world_list):
    world_list[i] = world_list[i].rstrip('\n')
    i += 1
team_name = input('Please enter the name of the team: ')
counter = 0
for i in world_list:
    if team_name == i:
        counter += 1
if counter == 0:
    print('The team you entered never won.')
else:
    print(f'The team you entered has won the World Series {counter} times.')

# 11
def is_Lo_Shu(matrix):
    matrix_sums = []
    for i in range(3):
        sums = 0
        for j in range(3):
            sums += matrix[i][j]
        matrix_sums.append(sums)
    for i in range(3):
        sums = 0
        for j in range(3):
            sums += matrix[j][i]
        matrix_sums.append(sums)
    sums = matrix[0][0] + matrix[1][1] + matrix[2][2]
    matrix_sums.append(sums)
    sums = matrix[0][2] + matrix[1][1] + matrix[2][0]
    matrix_sums.append(sums)
    sum_of_the_sum = 0
    for i in matrix_sums:
        sum_of_the_sum += i
    if sum_of_the_sum == 120:
        flag = True
    else:
        flag = False
    return flag
print(is_Lo_Shu([[4 , 9, 2], [3, 5, 7], [8, 1, 6]])) # Testing, this should display a value of True.

# 12
try:
    file_name = input('Please enter the name of the file: ')
    file_txt = open(file_name, 'r')
    file_list = file_txt.readlines()
    file_txt.close()
    i = 0
    while i < len(file_list):
        file_list[i] = file_list[i].rstrip('\n')  # FYI the clearing of a line is also done by the input function.
        i += 1
    number_of_lines = 0
    for i in file_list:
        number_of_lines += 1
except IOError:
    print("ERROR: Specified file name can't be found")
try:
    line_number = int(input('Please enter the line number you want to view: '))
    line_desired = file_list[line_number - 1]
    print('The data of the desired line is. ')
    print(line_desired)
except ValueError:
    print('ERROR, Please enter an integer value.')
except IndexError:
    print('ERROR, Please enter line number in the range of the data list. ')
except:
    print('An error has occured.')

# 13
def Magic_8_Ball():
    response = 'y'
    while response == 'y':
        import random
        number = random.randint(1, 12)
        random_txt = open('8_ball_responses.txt', 'r')
        random_txt_list = random_txt.readlines()
        i = 0
        while i < len(random_txt_list):
            random_txt_list[i] = random_txt_list[i].rstrip('\n')
            i += 1
        print('')
        print(random_txt_list[number-1])
        print('')
        response = input('Enter "y" if you wish to continue, \n Anything else if you wish to stop:')
Magic_8_Ball()

# 14
# Instead of typing it ourselves we can create the text file using a function.
# using random amounts of expense for each expense.
def expense_creator():
    import random
    expense_file = open('expenses_file.txt', 'w')
    new_list = []
    for i in range(6):
        expense = random.randint(500, 1000)
        new_list.append(str(expense) + '\n')
    expense_file.writelines(new_list)
    expense_file.close()
expense_creator()
expense_file = open('expenses_file.txt', 'r')
expense_list = expense_file.readlines()
i = 0
while i < len(expense_list):
    expense_list[i] = expense_list[i].rstrip('\n')
    i += 1
import matplotlib.pyplot as plt
plt.pie(expense_list)
plt.show()

# 15
# Instead of typing it ourselves we can create the text file using a function.
# using random amounts of expense for each expense.
def gas_price_creator():
    import random
    price_file = open('price_file.txt', 'w')
    new_list = []
    for i in range(52):
        price = random.randint(50, 80)
        new_list.append(str(price) + '\n')
    print(new_list)
    price_file.writelines(new_list)
    price_file.close()
gas_price_creator() # This function creates the gas price file for 1994
plot_file = open('price_file.txt', 'r')
price_file_list = plot_file.readlines()
i = 0
while i < len(price_file_list):
    price_file_list[i] = price_file_list[i].rstrip('\n')
    i += 1
print(price_file_list)
plot_file.close()
import matplotlib.pyplot as plt
x_coords = []
for i in range(1, 53):
    x_coords.append(i)
plt.plot(x_coords, price_file_list)
plt.xlim(xmin=0, xmax=53)
plt.ylim(ymin=0, ymax=53)
plt.title('1994 Weekly Gas Graph')
plt.xlabel('Week number.')
plt.ylabel('Gas Price.')
plt.grid('True.')
plt.show()
