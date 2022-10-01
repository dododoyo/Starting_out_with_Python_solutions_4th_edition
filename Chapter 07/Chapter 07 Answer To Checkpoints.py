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
# Will display the following output
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
Jasmine's family:
['Jim', 'Jill', 'John', 'Jasmine']

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
new_list = []
for i in range(3):
    for j in range(4):
        new_list[i][j] = 0




