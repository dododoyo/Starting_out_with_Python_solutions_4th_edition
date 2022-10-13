# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,C   6,D  
# 2,B   7,B   
# 3,A   8,A   
# 4,D   9,B  
# 5,C   10,A  

# ------- >>> Answer to True or False questions <<< ------- #

# 1,True 
# 2,False  
# 3,False  
# 4,False   

# ------- >>> Answer to Short answer questions < ------- #

# 1
# The base case of program 12-2 is that times is greater than zero.

# 2
# For this question the base case will be when n is equal zero and the
# recursive case will be when n is greater than zero.

# 3
# A recursion is not necessary to solve a problem problems with repetitive nature 
# can also be solved using loops.

# 4
# In a recursive function a function must call its smaller version to eventually reach 
# at the base case and prevent the program from executing forever.

# 5
# Problem can be reduced in recursion ny dividing it into smaller versions of the original.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
def main():
    word = 'test'
    show_me(word)
def show_me(word):
    print(word)
    new_word = word[1:]
    if len(new_word) > 0:
       show_me(new_word)
main()
# This program will display the following output.
test
est
st
t

# 2
def main():
    num = 10
    halver(num)
def halver(number):
    print(number)
    half = number / 2
    if half >= 1:
       halver(half)
main()
# When the following program is called the function halver will be called 4 times.

# 3
def queue(length):
    while length > 0:
       print('Please wait.')
       length = length - 1
    print('It is your turn.')
# The recursive form of the above function is:
def recursive_queue(length):
    if length > 0:
        print('Please wait.')
        recursive_queue(length-1)
    else:
        print('It\'s your turn')
