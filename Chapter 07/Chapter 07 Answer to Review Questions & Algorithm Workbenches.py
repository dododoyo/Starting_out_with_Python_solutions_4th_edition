# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,A   6,C   11,A
# 2,B   7,B   12,B
# 3,C   8,D   13,C
# 4,D   9,C   14,D
# 5,B   10,B


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,True
# 2,True    7,True
# 3,False   8,False
# 4,True
# 5,False


# ------- >>> Answer to Short answer questions < ------- #

# 1
# a) The list has five elements.
# b) The index of the first element is 0.
# c) The index of the last element is 4.

# 2
# 'B'
# 'D'
# 'C'

# 3
values = [2, 4, 6, 8, 10]
print(values[1:3])
# Will display the following output
[4, 6]

# 4
numbers = [5, 4, 3, 2, 1, 0]
print(numbers[:3])
# Will display the following output
[5, 4, 3]

# 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[-4:])
# Will display the following output
[5, 6, 7, 8]

# 6
values = [2] * 5
print(values)
# Will display the following output
[2, 2, 2, 2, 2]

# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
list = []
for i in range(1, 101, 1):
    list.append(i)

# 2
for i in names:
    print(i)

# 3
scores.sort()
scores.reverse()
biggest = max(scores)
print(biggest)

# 4
# The function will be as follows.
accumulator = 0
for i in list:
    accumulator += i
# flowchart is hard to show here

# 5
def adding_machine(the_list):
    accumulator = 0
    for l in the_list:
        accumulator += l
    return accumulator

# 6
if 'Ruby' in names:
    print('Hello Ruby')
else:
    print('No Ruby.')

# 7
list1 = [1, 2, 1, 2]
list2 = [3, 1, 2, 1, 2]

# 8
new_list = []
new_inner_list = []
for i in range(5):
    new_inner_list = []
    for j in range(3):
        new_inner_list.append(0)
    new_list.append(new_inner_list)
print(new_list)
for i in range(5):
    for j in range(3):
        values = int(input(f'Please enter the value for row {i+1} column {j+1}.'))
        new_list[i][j] = values
