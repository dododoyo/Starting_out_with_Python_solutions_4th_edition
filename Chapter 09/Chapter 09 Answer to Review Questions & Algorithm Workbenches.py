# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   6,A   11,C   16,B
# 2,D   7,D   12,B   17,D
# 3,B   8,C   13,A
# 4,A   9,B   14,A
# 5,C   10,B  15,C


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,True
# 2,True    7,False
# 3,False   8,True
# 4,False   9,False
# 5,False   10,True


# ------- >>> Answer to Short answer questions < ------- #

# 1
dct = {'Monday':1, 'Tuesday':2, 'Wednesday':3}
print(dct['Tuesday'])
# The above code will display the following output.
# 2

# 2
dct = {'Monday':1, 'Tuesday':2, 'Wednesday':3}
print(dct.get('Monday', 'Not found'))
# The above code will display the following output.
# 1

# 3
dct = {'Monday':1, 'Tuesday':2, 'Wednesday':3}
print(dct.get('Friday', 'Not found'))
# The above code will display the following output.
# Not found

# 4
months = {'Jan':1, 'Feb':2, 'Mar':3}
months[2]
# When the above code is executed KeyError will occur.

# 5
# We can delete an element from a dictionary using the del
# statement and specifing the key.

# 6
# You can determine the number of elements stored in a dictionary 
# using the built in len function.

# 7
dct = {0:[1, 2, [3, 4], 5]}
print(dct[0][2][1])
# The above code will display 
# 4

# 8
dct = {1:[0, 1], 2:[2, 3], 3:[4, 5]}
for k in dct:
    print(k)
# The above code will display the following output
# 1
# 2
# 3

# 9
myset = set('Saturn')
# After the above statement executes myset = {'S', 'a', 't', 'u', 'r', 'n'}

# 10
myset = set(10)
# After the above statement executes no elements will be stored in the set 
# because the object 10 is not iterable and this code will show TypeError

# 11
myset = set('a bb ccc dddd')
# After the above statement executes myset = {'a', 'b', 'c', 'd', ' '}

# 12
myset = set([2, 4, 4, 6, 6, 6, 6])
# After the above statement executes myset = {2, 4, 6}

# 13
myset = set(['a', 'bb', 'ccc', 'dddd'])
# After the above statement executes myset = {'ccc', 'dddd', 'a', 'bb'}

# 14
myset = set('1 2 3')
print(len(myset))
# The above code will display the following output
# 4

# 15
set1 = set([10, 20, 30, 40])
set2 = set([40, 50, 60])
set3 = set1.union(set2)
# After the above code executes set3 = {10, 20, 30, 40, 50, 60}

# 16
set1 = set(['o', 'p', 's', 'v'])
set2 = set(['a', 'p', 'r', 's'])
set3 = set1.intersection(set2)
# After the above code executes set3 = {'p', 's'}

# 17
set1 = set(['d', 'e', 'f'])
set2 = set(['a', 'b', 'c', 'd', 'e'])
set3 = set1.difference(set2)
# After the above code executes set3 = {'f'}

# 18
set1 = set(['d', 'e', 'f'])
set2 = set(['a', 'b', 'c', 'd', 'e'])
set3 = set2.difference(set1)
# After the above code executes set3 = {'a', 'b', 'c'}

# 19
set1 = set([1, 2, 3])
set2 = set([2, 3, 4])
set3 = set1.symmetric_difference(set2)
# After the above code executes set3 = {1, 4}

# 20
set1 = set('abc')
set2 = set('def')
# Since they share no common member the result of calculating their intersection 
# will be an empty set. and set1&set2 will produce same result as the union.

# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
dictionary = {'a':1, 'b':2, 'c':3}

# 2
dictionary = {}

# 3
if 'James' in dct:
    print(dct['James'])
else:
    print("This key doesn't exist in the dictionary")

# 4
if 'Jon' in dct:
    jon_value = dct['Jon']
    dct['John'] = jon_value
    del dct['jon']

# 5
game =set(['rock', 'paper', 'scissors'])

# 6
# Assuming each variable set1 and set2 references a set.
set3 = set1.union(set2)
# The above code will create a set containing all elements of set1 and set2

# 7
# Assuming each variable set1 and set2 references a set.
set3 = set1.intersection(set2)
# The above code will create a set containing elements both in set1 and set2

# 8
# Assuming each variable set1 and set2 references a set.
set3 = set1.difference(set2)
# The above code will create a set containing elements in set1 but not in set2

# 9
# Assuming each variable set1 and set2 references a set.
set3 = set2.difference(set1)
# The above code will create a set containing elements in set2 but not in set1

# 10
for i in set1:
    if i > 100:
        set2.add(i)

# 11
import pickle
dct = {1, 2, 3, 4} # Sample dictionary
new_file = open('mydata.dat', 'wb')
pickle.dump(dct, new_file)

# 12
import pickle
new_file = open('mydata.dat', 'rb')
dct = pickle.load(new_file)
print(dct)
