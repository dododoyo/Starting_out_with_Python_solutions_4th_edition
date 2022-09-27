# ------- >>> Answer to Checkpoints <<< ------- #


# 1 => Output file is a file data is written on.

# 2 => Input file is a file data is read from.

# 3 => open the file -> process the file -> close the file

# 4 => The two types of file are text fie and binary file-
# binaryfile is a file whose content must be interpreted by a program or a
# hardware processor that understands in advance exactly how it is formatted
# textfile is a type of digital, non-executable file that contains letters, numbers, symbols and/or a combination.

# 5 There are two types of file access
# sequential access(accessing from beginning to the end of the file)
# direct access(can jump to any piece of data inside the file)

# 6 the two file associated names are
# file variable - name of the variable that will reference the object
# file name - string specifying the name of the file

# 7 It wil erase all it's contents

# 8 For creating a file object and associating it with a file on the disk.

# 9 To disconnect program from the file and prevent loss of data fromm the buffer.

# 10 If location is not specified python interpreter assumes files location is same as the program.

# 11 We must open it in append mode, the data will be added to the end of the file.

# 12
tmp_local = open('philosophers.txt', 'w')
for i in range(1, 11):
    tmp_local.write(str(i) + '\n')
tmp_local.close()

# 13 It means the file has no data or the current line contains no text

# 14
temp_loc = open('data.txt', 'r')
line1 = temp_loc.readline()
while line1 != '':
    print(line1)
    line = temp_loc.readline()
temp_loc.close()

# 15
tempo_loc = open('data.txt', 'r')
for line2 in tempo_loc:
    print(line2)
tempo_loc.close()

# 16
# record is a complete set of data about a specific item
# field is a single piece of data within a record

# 17
# First create a second temporary file. copy all of original file's record
# to the temporary file but when you get to the item to be modified you write the new
# instead and continue to copy the rest of the file. After finishing delete the old file
# and rename the new with the old ones name.

# 18
# This happens because you can't read and write a text with python at the same time.

# 19
# exception is an error that occurs while a program is running

# 20
# In most cases it will force the program to halt.

# 21
# IOError occurs when a code tries to open a file that doesn't exist

# 22
# ValueError occurs when user gives invalid  value to a function.