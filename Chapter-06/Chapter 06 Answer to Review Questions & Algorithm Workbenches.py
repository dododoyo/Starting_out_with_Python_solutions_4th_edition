# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   6,B   11,B
# 2,A   7,D   12,A
# 3,D   8,C   13,B
# 4,C   9,A   14,C
# 5,A   10,D  15,B


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,False
# 2,True    7,True
# 3,False   8,False
# 4,True    9,False
# 5,False


# ------- >>> Answer to Short answer questions < ------- #

# 1
# open file - creates connection between the data and python allowing it to read or write data to the file
# process file - data is either written or read from the file
# close file - disconnects file from the program

# 2
# To free up some resources your program is using while processing file
# and prevent loss of some data.

# 3
# read position is marker of location of the next item that will be read from a file
# read position's initial location is at the beginning the file

# 4
# the 'w'(write) mode should be opened to allow data to be written to it, erasing any previous data.

# 5
# program will show IOError


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
new_var = open('things.txt', 'w')
new_var.write('Giraffe \n')
new_var.write('Pineapple \n')
new_var.write('Brazil \n')
new_var.close()

# 2
new_file = open('things.txt', 'r')
line_1 = new_file.readline()
line_2 = new_file.readline()
line_3 = new_file.readline()
new_file.close()
print(line_1)
print(line_2)
print(line_3)

# 3
number_list = open('number_list', 'w')
for i in range(1, 101):
    number_list.write(str(i) + '\n')
number_list.close()

# 4
show_list = open('number_list.txt', 'r')
for line in show_list:
    print(line)
show_list.close()

# 5
list_show = open('number_list.txt', 'r')
counter = 0
for line3 in list_show:
    counter += int(line3)
print(counter)
list_show.close()

# 6
new_var1 = open('number_list', 'a')  # this code will open file without erasing
# it's contents, if they exist
new_var1.close()  # even if not asked it's preferable if you close the file

# 7
import os
found = False
stud_hold = open('students.txt', 'r')
new_hold = open('newfile.txt', 'w')
newline3 = stud_hold.readline()
while newline3 != '':
    points = stud_hold.readline()
    newline3 = newline3.rstrip('\n')
    if newline3 != 'John Perz':
        new_hold.write(newline3 + '\n')
        new_hold.write(points)
    else:
        found = True
    newline3 = stud_hold.readline()
stud_hold.close()
new_hold.close()
os.remove('students.txt')
os.rename('newfile.txt', 'students.txt')
if found:
    print('Found and deleted')
else:
    print('not found')

# 8
import os
found = False
new_buff = open('students.txt', 'r')
another_one = open('another_one.txt', 'w')
buff_line = new_buff.readline()
while buff_line != '':
    buff_line = buff_line.rstrip('\n')
    points = new_buff.readline()
    if buff_line != 'Julie Milan':
        another_one.write(buff_line + '\n')
        another_one.write(points)
    else:
        another_one.write(buff_line + '\n')
        another_one.write('100')
        found = True
    buff_line = new_buff.readline()
new_buff.close()
another_one.close()
os.remove('students.txt')
os.rename('another_one.txt', 'students.txt')
if found:
    print('Found and updated')
else:
    print('not found')

# 9
# the given code wil show the following output
# >>This code caused a ValueError
# >>The end

# 10
# the given code will show the following output
# >>This code caused a NameError
