# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   
# 2,C  
# 3,B  
# 4,A   
# 5,C   

# ------- >>> Answer to True or False questions <<< ------- #

# 1,True
# 2,False
# 3,True
# 4,False
# 5,False

# ------- >>> Answer to Short answer questions < ------- #

# 1
# A subclass inherits the attributes of the superclass.

# 2
# class Hammer(Tool):
# From the class defination given above Tool is the name of the superclass, and Hammer is the name of the subclass.

# 3
# An overridden method is a method that exists in a super class ,and has been duplicated in the defination of the subclass.


# ------- >>> Answer to Algorithm Workbench Questions < ------- #

# 1
class Trout(Fish):
# This is first line of the definition for a Trout subclass, having Fish as a superclass.

# 2
class Art:
    def __init__(self, art_type):
        self.__art_type = art_type
    def message(self):
        print("I'm a piece of art.")

class Painting(Art):
    def __init__(self):
        Art.__init__(self, 'painting')
    def message(self):
        print("I'm a painting.")
a = Art('sculpture')
p = Painting()
a.message()
p.message()
# The following class definition and statements will display the following output.
I'm a piece of art.
I'm a painting.

# 3
class Bird:
    def __init__(self, bird_type):
        self.__bird_type = bird_type
    def __str__(self):
        return self.__bird_type
class Duck(Bird):
    def __init__(self):
        Bird.__init__(self, 'duck')

