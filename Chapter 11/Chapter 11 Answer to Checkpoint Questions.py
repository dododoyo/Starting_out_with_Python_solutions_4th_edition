# 1
# A specialized class is is a subclass. The general class is called the superclass.

# 2
# When we say there is an "is a"  relation ship between two objects it means the specialized class has 
# all of the attributes of the superclass.

# 3
# A subclass inherits all of it's superclass's attributes.

# 4
# The name of the super class is Bird the name of the subclass is Canary.

# 5
class Vegetable:
    def __init__(self, vegtype):
        self.__vegtype = vegtype
    def message(self):
        print("I'm a vegetable.")
class Potato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self, 'potato')
    def message(self):
        print("I'm a potato.")
    
v = Vegetable('veggie')
p = Potato()
v.message()
p.message()
# The following class definition and statments will display the following output.
# I'm a vegetable.
# I'm a potato.
