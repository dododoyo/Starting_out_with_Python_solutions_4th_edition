# ------- >>> Answer to Checkpoints <<< ------- #

# 1
numbers = [1, 2, 3, 4, 5]
numbers[2] = 99
print(numbers)
# Will display the list
[1, 2, 99, 4, 5]


# 2
numbers = list(range(3))
print(numbers)
# Will display the list
[0, 1, 2]

# 3
numbers = [10] * 5
print(numbers)
# Will display the list
[10, 10, 10, 10, 10]

# 4
numbers = list(range(1, 10, 2))
for n in numbers:
    print(n)
# Will display the following lines of output
1
3
5
7
9

# 5
numbers = [1, 2, 3, 4, 5]
print(numbers[-2])
# Will display the following output
4

# 6
# To find the number of elements in a list a programmer can either use
# loops to find the number of elements or the built in len() function

# 7
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = numbers1 + numbers2
print(numbers1)
print(numbers2)
print(numbers3)
# Will display the following list of lists
[1, 2, 3]
[10, 20, 30]
[1, 2, 3, 10, 20, 30]

# 8
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers2 += numbers1
print(numbers1)
print(numbers2)
# Will display the following output
[1, 2, 3]
[10, 20, 30, 1, 2, 3]

# 9
numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:3]
print(my_list)
# Will display the following output
[2, 3]

# 10
numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:]
print(my_list)
# Will display the following output.
[2, 3, 4, 5]

# 11
numbers = [1, 2, 3, 4, 5]
my_list = numbers[:1]
print(my_list)
# Will display the following output
[1]

# 12
numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)
# Will display the following output
[1, 2, 3, 4, 5]

# 13
numbers = [1, 2, 3, 4, 5]
my_list = numbers[-3:]
print(my_list)
# Will display the following output
[3, 4, 5]

# 14
names = ['Jim', 'Jill', 'John', 'Jasmine']
if 'Jasmine' not in names:
   print('Cannot find Jasmine. ')
else:
    print("Jasmine's family: ")
    print(names)
# Will display the following output
#Jasmine's family:
#['Jim', 'Jill', 'John', 'Jasmine']

# 15
# The difference between list's remove method and del method
# is that remove method specifies the item to remove it from the list
# while the del method specifies the item's index to remove it.

# 16
# The highest and the lowest values can be found using the min() and max() functions.

# 17
# Both statements can be used to add the string to the list index 0

# 18
# a) index method is used to find the index of a specified item in a list.
# b) insert method is used to insert an item to a list at a specified index.
# c) sort method is used to sort the items in a list in ascending order.
# d) reverse method is used to reverse the order of the items in a list.

# 19
# The two dimensional list given in checkpoint 7.19 has 4 rows and 2 colomuns

# 20
inner_list = []
new_list = []
for i in range(3):
    new_list.append(inner_list)
    for j in range(4):
        inner_list.append(0)
    inner_list = []

# 21
# For each element within the matrix
for i in range(3):
    for j in range(4):
        print(new_list[i][j])
# For each row in the matrix
for i in range(3):
    print(new_list[i])

# 22
# The primary difference between a list and a tuple is that list is mutable.

# 23
# Tuples exist because they are easier and faster to process, and are
# safe because thier contents can't be mutable.

# 24
my_list = tuple(my_list)

# 25
my_list = list(my_list)

# 26
# To create a graph with the plot function the two arguments you will
# need is the x and y coordinates of the plot.

# 27
# The plot function produces a line graph.

# 28
# You can use the xlabel() and the ylabel() functions to add labels
# to the x and y axis respectively.

# 29
# You can customize the lower and upper limits of the X and Y axes by calling the
# xlim and ylim functions.

# 30
# The tick marks can be customized by using marker arguments
# listed in the book

# 31
# To create the bar function we pass the left corner of our bar and its
# height to the bar method.

# 32
# The bars will have colors red, blue, red, blue

# 33
# To create a pie chart we pass the list of values as an argument.
