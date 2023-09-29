# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   6,D   11,D
# 2,D   7,C   12,A
# 3,C   8,A  
# 4,D   9,B   
# 5,B   10,A


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False   6,True
# 2,True    7,False
# 3,False  
# 4,False
# 5,True


# ------- >>> Answer to Short answer questions < ------- #

# 1
# Data hiding is just another name for the process of making an attribute private.

# 2
# Data attributes can be made inaccesible by making them private to the class.

# 3
# A class is a general map for the instances to be created by it. Just like the blueprint
# and house example given in the text class is the blueprint instance is the house.

# 4
# wallet.get_dollar()
# from the above code wallet is the name of the variable that references the object
# and get_dollar is name of the method 

# 5
# When the __init__ method executes the self parameter will reference the object 
# that was created by the class.

# 6
# In python you can hide an attribute from code outside by starting the name of the
# attribute by two underscore characters

# 7
# __str__ method can be used by passing it as an argument in the print function.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
class Book:
    def __init__(self, title, author_name, pages):
        self.__title = title
        self.__name = author_name
        self.__pages = pages
    def __len__(self):
        return self.__pages
    def __str__(self):
        return 'Title of the book is: ' + self.__title + \
            '\nAuthor of the book is: ' + self.__name + \
            '\nThe number of pages is: ' + self.__pages 

# 2
class Book:
    def __init__(self, title, author_name, publisher_name):
        self.__title = title
        self.__name = author_name
        self.__publisher = publisher_name
    def get_title(self):
        return self.__title
    def get_publisher(self):
        return self.__publisher
    def get_name(self):
        return self.__name
    def set_title(self, title):
        self.__title = title
    def get_publisher(self, publisher_name):
        self.__publisher = publisher_name
    def set_name(self, name):
        self.__name = name
    def __str__(self):
        return 'Title of the book is: ' + self.__title + \
            '\nAuthor of the book is: ' + self.__name + \
            '\nThe publisher of the book is : ' + self.__publisher

# 3
# a) The potential class in the given problem domain is the types of accounts and a customer checkin accounts,
# savings accounts, and money market accounts. 
# b) I think the only class we will need is the accounts class because for each of the type of account
# we can specify the atributes that will make it a different type account
# c) The reponsibility of the class will be to get the initial balance of the account
# get what type account it is , earn interest on the money depending on the time, withdraw money form
# the account, know what amounnt of main is in the account depending on the time
