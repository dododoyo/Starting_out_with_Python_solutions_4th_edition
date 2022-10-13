# ------- >>> Answer to Checkpoints <<< ------- #
# 1
# An element in a dictionary has two parts called the key and the value

# 2
# The key of an element in a dictionary must be immutable object.

# 3
# The key value is 'start'

# 4
# The statement adds an element with key 'id' and value 54321 to the dictionary.

# 5
stuff = {1 : 'aaa', 2 : 'bbb', 3 : 'ccc'}
print(stuff[3])
# The following code will display. 
# ccc

# 6
# You can check if a key-value pair exists in a dictionary using
# the in operator with the key of the specified element

# 7
inventory ={}
del inventory[654]
# Supposing the dictionary exists the statement above removes an
# element associated with the key 654

# 8
stuff = {1 : 'aaa', 2 : 'bbb', 3 : 'ccc'}
print(len(stuff))
# The following code will display the amount of elements in the dictonary.
# which is 3.

# 9
stuff = {1 : 'aaa', 2 : 'bbb', 3 : 'ccc'}
for k in stuff:
    print(k)
# The following code will display
# 1
# 2
# 3

# 10
# The pop method removes an element with a specified with a key
# The popitem method removes the last element.

# 11
# Returns all the elements in a dictionary and their associated values
# as a sequence of tuples.

# 12
# Returns all the keys in a dictionary as a sequence of tuples.

# 13
# Returns all the values in a dictionary as a sequence of tuples.

# 14
# Since elements in a set are stored in no particular order the elements in a set are unordered.

# 15
# The elements in a set must have a unique value it is not allowed to store duplicate items in a set.

# 16
# using the built in set function you can create an empty set.

# 17
myset = set('Jupiter')
# After the following statement each character of the string will be stored as an element in the set.

# 18
# The statement in checkpoint 9.18 will show an error because the argument provided is not iterable.

# 19
myset = set('www xxx yyy zzz')
# After this statement executes 'w' 'x' 'y' 'z' ' ' will be the elements in the set.
# or myset = {'w', 'x', 'y', 'z', ' '}

# 20
myset = set([1, 2, 2, 3, 4, 4, 4])
# After this statement executes '1' '2' '3' '4' will be the elements in the set.
# or myset = {'1', '2', '3', '4'}

# 21
myset = set(['www', 'xxx', 'yyy', 'zzz'])
# After this statement executes 'www' 'xxx' 'yyy' 'zzz' will be the elements in the set.
# or myset = {'www', 'xxx', 'yyy', 'zzz'}

# 22
# You can determine the number elements in a set using the builtin len function.

# 23
myset = set([10, 9, 8])
myset.update([1, 2, 3])
# After this statement executes myset = {1, 2, 3, 8, 9, 10}

# 24
myset = set([10, 9, 8])
myset.update('abc')
# After this statement executes myset = {'a', 'b', 'c', 8, 9, 10}

# 25
# The only difference between a remove and a discard method is in thier response when
# the item to be removed is not found remove method raise a keyvalue error while discard doesn't

# 26
# You can use the in operator to check if an element exists in a set or not.

# 27
set1 = set([10, 20, 30])
set2 = set([100, 200, 300])
set3 = set1.union(set2)
# After this statement executes set3 = {10, 20, 30, 100, 200, 300}

# 28
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1.intersection(set2)
# After this statement executes set3 = {3, 4}

# 29
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1.difference(set2)
# After this statements execute set3 = {1, 2}

# 30
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set2.difference(set1)
# After this statements execute set3 = {5, 6}

# 31
set1 = set(['a', 'b', 'c'])
set2 = set(['b', 'c', 'd'])
set3 = set1.symmetric_difference(set2)
# After this statements execute set3 = {a, d}

# 32
set1 = set([1, 2, 3, 4])
set2 = set([2, 3])
# From the sets given above set2 is the subset of set1
# and set1 is the superset of set2.

# 33
# Serialization is the process of converting an object in a stream of bytes.

# 34
# When openning a file for the purpose of saving a pickled object we use the 'wb' mode.

# 35
# When openning a file for the purpose of retrieving a pickled object we use the 'rb' mode.

# 36
# When we want to pickle object we import the pickle module.

# 37
# To pickle an object you call the dump function from the pickle module.

# 38
# To retrieve and unpickle and object we use the load function.
