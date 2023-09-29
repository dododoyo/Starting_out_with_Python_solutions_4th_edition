#   ------- >>> Answer to Programming Exercises <<< ------- #
# 1
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
    def get_shift(self):
        return self.__shift_number
    def get_rate(self):
        return self.__pay_rate
    def set_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    def set_shift(self, shift_number):
        self.__shift_number = shift_number

name1 = input('Please enter the name of the employee: ')
number1 = input('Please enter employee\'s number.')
shift = int(input('Please enter "1" for day shift and "2" for night shift: '))
pay_rate1 = float(input('Please enter the hourly pay rate: '))
employee1 = ProductionWorker(name1, number1, shift, pay_rate1)

print('')
print('Name of the employee is', employee1.get_name())
print('Having employee number', employee1.get_number())
print('Hourly pay rate of the employee is', employee1.get_rate())
shift = employee1.get_shift()
if shift == 1:
    print('The employee works at the day shift.')
else:
    print('The employee works at the night shift.')

# 2
class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, production_bonus):
        Employee.__init__(self, name, number)
        self.__annual_salary = annual_salary
        self.__production_bonus = production_bonus
    def get_salary(self):
        return self.__annual_salary
    def get_bonus(self):
        return self.__production_bonus
    def set_rate(self, annual_salary):
        self.__annual_salary = annual_salary
    def set_shift(self, production_bonus):
        self.__production_bonus = production_bonus


name2 = input('Please enter the name of the employee: ')
number2 = input('Please enter employee\'s number: ')
annual_salary2 = int(input('Please enter the annual salary: '))
production_bonus = float(input('Please enter the production bonus of the supervisor: '))
employee2 = ShiftSupervisor(name2, number2, annual_salary2, production_bonus)
print('')
print('Name of the employee is', employee2.get_name())
print('Having employee number', employee2.get_number())
print('Annual salary of the employee is', employee2.get_salary())
print('The yearly bonus of the employee is: ', employee2.get_bonus())

# 3
class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone
class Customer(Person):
    def __init__(self, name, address, phone, mailing):
        Person.__init(self, name, address, phone)
        self.__mailing = mailing
    def set_mailing(self, mailing):
        self.__mailing = mailing
    def get_mailing(self):
        return self.__mailing