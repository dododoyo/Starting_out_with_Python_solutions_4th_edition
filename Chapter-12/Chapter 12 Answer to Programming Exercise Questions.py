#   ------- >>> Answer to Programming Exercises <<< ------- #

# 1
def recurse_printer(number1):
    if number1 >= 0:
        print(number1)
        recurse_printer(number1-1)

# 2
def recur_multiplyer(x, y):
    if x == 1 and y > 1:
        return y
    elif  y == 1 and x > 1:
        return x
    elif x == 1 and y == 1:
        return x
    else:
        y + recur_multiplyer(x-1, y)

# 3
def recursive_max(the_list):
    if len(the_list) == 1:
        return the_list[0]
    else:
        m = recursive_max(the_list[1:])
        if m > the_list[0]:
            return m
        else:
            return the_list[0]

# 4
def recursive_adder(the_list):
    if len(the_list) == 1:
        return the_list[0]
    else:
        return the_list[0] + recursive_adder(the_list[1:])

# 5
def is_palidrome(the_string):
    if len(the_string) < 1:
        return True
    else:
        if the_string[0] == the_string[-1]:
            return is_palidrome(the_string[1:-1])
        else:
            return False

# 6
def power(x,y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x * power(x, y-1)

# 7
def ackermann(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))
        