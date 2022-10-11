# 1
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
name_ = input('Please enter the name of your pet: ')
age_ = input('Please enter the age of your pet: ')
type_ = input('Please enter the type of the pet: ')
the_pet = Pet(name_, type_, age_)
print('The name of you pet is ', the_pet.get_name())
print('Your pet is a/an', the_pet.get_animal_type())
print('The age of your pet is', the_pet.get_age())

# 2
class Car:
    def __init__(self, year_model, make, speed):
        speed = 0
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed  -= 5
    def get_speed(self):
        return self.__speed
my_car = Car('2020', 'Toyota' , '15')
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
print(my_car.get_speed())
my_car.brake()
my_car.brake()
my_car.brake()
my_car.brake()
my_car.brake()
print(my_car.get_speed())

# 3
class PersonalInfo:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone_number
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_number(self, phone_number):
        self.__phone = phone_number
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__age
    def get_address(self):
        return self.__address
    def get_phone_number(self):
        return self.__phone

person1 = PersonalInfo('Dolphin', 'Bole', '20', '000000000')
person2 = PersonalInfo('Tony', 'America', '87', '12123954')
person3 = PersonalInfo('Hello', 'Ethiopia', '65', '123456')

# 4
class Employee:
    def __init__(self, name, ID_Number, Department, Job_title):
        self.__name = name
        self.__idnum = ID_Number
        self.__department = Department
        self.__job_title = Job_title
    def __str__(self):
        return ' Name of the employee is ' + self.__name + \
               '\n The ID number of employee is ' + str(self.__idnum) + \
               '\n The employee is under the department ' + self.__department + \
               '\n The job title of the employee is ' + self.__job_title + \
                '\n'
employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
employee2 = Employee('Mark Jones', 39119, "IT", 'Programmer')
employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
print(employee1)
print(employee2)
print(employee3)

# 5
class RetailItem:
    def __init__(self, description, unit_invertory, price):
        self.__description = description
        self.__units = unit_invertory
        self.__price = price
    def __str__(self):
        return ' The item is a\\an'+ self.__description + \
            '\n The number of items left in the invertory is' + str(self.__units)+ \
            '\n The price of an individual item is' + str(self.__price)
item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40, 34.95)
item3 = RetailItem('Shirt', 20, 24.95)

# 6
class Patients:
    def __init__(self, first_name, middle_name, last_name, address, city, zip_code, phone_number, name_emergency, emergency_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__zip = zip_code
        self.__phone_number = phone_number
        self.__name_emergency = name_emergency
        self.__emergency_phone = emergency_phone
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, middle_name):
        self.__middle_name = middle_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_address(self, address):
        self.__address = address
    def set_city(self, city):
        self.__city = city
    def set_zip_code(self, zip_code):
        self.__zip = zip_code
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    def set_emergency_name(self, name_emergency):
        self.__name_emergency = name_emergency
    def set_emergency_phone(self, emergency_phone):
        self.__emergency_phone = emergency_phone 
    def get_first_name(self):
        return self.__first_name 
    def get_last_name(self):
        return self.__middle_name 
    def get_last_name(self):
        return self.__last_name 
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city 
    def get_zip_code(self):
        return self.__zip 
    def get_phone_number(self):
        return self.__phone_number
    def get_emergency_name(self):
        return self.__name_emergency 
    def get_emergency_phone(self):
        return self.__emergency_phone
class Procedure:
    def __init__(self, procedure_name, date, practitioner_name, charges):
        self.__procedure_name = procedure_name
        self.__practitioner_name = practitioner_name
        self.__date = date
        self.__charges = charges
    def get_date(self):
        return self.__date
    def get_prodcedure_name(self):
        return self.__procedure_name
    def get_practitioner_name(self):
        return self.__practitioner_name
    def get_charges(self):
        return self.__charges
    def set_date(self, date):
        self.__date = date
    def set_procedure_name(self, procedure_name):
        self.__practitioner_name = procedure_name
    def set_practitioner_name(self, practitioner_name):
        self.__practitioner_name = practitioner_name
    def set_charges(self, charges):
        self.__charges = charges
procedure1 = Procedure('Physical Exam', 'oct-9-2002', 'Dr. Irvine', 250.00)
procedure2 = Procedure('X-ray', 'oct-9-2022', 'Dr.Jamison', 500.00)
procedure3 = Procedure('Blood test', 'oct-9-2022', 'Dr. Smith', 200.00)
patient = Patients('Chris', 'Drake', 'Brown', 'Arizona', 'California', 1235, 293940322, 'DJ-Khalid', 89473982)
print('Patient\'s name is', patient.get_first_name() +" "+ patient.get_last_name() )
print('Patient\'s address is', patient.get_address() + ' '+ patient.get_city())
print('Patient\'s phone number is', patient.get_phone_number())
print('Name of patient\'s emergency contact is',patient.get_emergency_name())
print('Phone of the emergency contact is', patient.get_emergency_phone()) 
print('\n')

print('The details of the first procedure is')
print('Procedure name: ', procedure1.get_prodcedure_name())
print('Date:', procedure1.get_date())
print('Practitioner:', procedure1.get_practitioner_name())
print('Charge:',procedure1.get_charges())
print('\n')
print('The details of the second procedure is')
print('Procedure name: ', procedure2.get_prodcedure_name())
print('Date:', procedure2.get_date())
print('Practitioner:', procedure2.get_practitioner_name())
print('Charge:',procedure2.get_charges())
print('\n')
print('The details of the third procedure is')
print('Procedure name: ', procedure3.get_prodcedure_name())
print('Date:', procedure3.get_date())
print('Practitioner:', procedure3.get_practitioner_name())
print('Charge:',procedure3.get_charges())
print('\n')
print('The total charge of the procedures is:')
print('------------------------------------')
total_charge = procedure1.get_charges() + procedure2.get_charges() + procedure3.get_charges()
print(total_charge)


# 7
import pickle
class Employee:
    def __init__(self, name, ID_Number, Department, Job_title):
        self.__name = name
        self.__idnum = ID_Number
        self.__department = Department
        self.__job_title = Job_title
    def get_name(self):
        return self.__name
    def get_idnum(self):
        return self.__idnum
    def get_department(self):
        return self.__department
    def get_job_title(self):                   
        return self.__job_title
    def set_name(self, name):
        self.__name = name
    def set_idnum(self, ID_Number):
        self.__idnum = ID_Number
    def set_department(self, Department):
        self.__department = Department
    def set_job_title(self, Job_title):
        self.__job_title = Job_title
    def __str__(self):
        return ' Name of the employee is ' + self.__name + \
               '\n The ID number of employee is ' + str(self.__idnum) + \
               '\n The employee is under the department ' + self.__department + \
               '\n The job title of the employee is ' + self.__job_title + \
                '\n'
employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
employee2 = Employee('Mark Jones', 39119, "IT", 'Programmer')
employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')


def Employee_management():
    file_name = input('Please enter the name of the file you like to access: ')
    try:
        file_object = open(file_name, 'rb')
        employees = pickle.load(file_object)
        file_object.close()
    except FileNotFoundError:
        employees = {}
    choice = 1
    while choice != 5:
        print('')
        print('Below is the list of task to do and their related number')
        print('-------------------------------------------------')
        print('1 \t \t Look up an Employee.')
        print('2 \t \t Add a new Employee.')
        print('3 \t \t Edit Employee details.')
        print('4 \t \t Delete an Employee.')
        print('5 \t \t Quit the program.')
        choice = int(input('Please enter the number of your choice: '))
        while choice > 5 or choice < 1:
            print('Invalid value:  ')
            print('')
            print('Below is the list of task to do and their related number')
            print('-------------------------------------------------')
            print('1 \t \t Look up an Employee.')
            print('2 \t \t Add a new Employee.')
            print('3 \t \t Edit Employee details.')
            print('4 \t \t Delete an Employee.')
            print('5 \t \t Quit the program.')
            choice = int(input('Please enter the number of your choice: '))
        if choice == 1:
            print('')
            name_ = input('Please enter the name of employee you like to look up: ')
            if name_ in employees:
                print(employees[name_])
            else:
                print('Employee doesn\'t  work here.')
        elif choice == 2:
            print('')
            name_ = input('Please enter name of the person you like to add: ')
            id_num = input('Please enter the ID number of the employee:')
            department = input('Please enter department the employee is in: ')
            job_title = input('Please enter the job title of the employee: ')
            another_employee = Employee(name_, id_num, department, job_title)
            employees[name_] = str(another_employee)
            print('Employee information was successfully added.')
        elif choice == 3:
            print('')
            name_ = input('Please enter the name of employee you like to edit: ')
            id_num = input('Please enter the new ID number of the employee: ')
            department = input('Please enter the new department the employee is in: ')
            job_title = input('Please enter the new job title of the employee:  ')
            another_employee = Employee(name_, id_num, department, job_title)
            employees[name_] = str(another_employee)
            print('Employee information was successfully edited.')
        elif choice == 4:
            print('')
            name_ = input('Please enter the name of the employee you like to deleted: ')
            del employees[name_]
            print('Employee\'s information was successfully deleted.' )
        else:
            file_object = open(file_name, 'wb')
            pickle.dump(employees, file_object)
            file_object.close()
            print('')
            print('That will be all for today, Thank You.')
            print('')


Employee_management()

# 8
# In this program i putted both the classes in the same program. alternatively
# we can import the retailitem class as module, either way the function is the same.abs(x)
class RetailItem:
    def __init__(self, description, unit_invertory, price):
        self.__description = description
        self.__units = unit_invertory
        self.__price = price
    def set_price(self, price):
        self.__price = price
    def set_units(self, unit_invertory):
        self.__units = unit_invertory
    def set_description(self, description):
        self.__description = description
    def get_price(self):
        return self.__price
    def get_units(self):
        return self.__units
    def get_description(self):
        return self.__description
    def __str__(self):
        return ' The item is a\\an '+ self.__description + \
            '\n The number of items left in the invertory is' + str(self.__units)+ \
            '\n The price of an individual item is' + str(self.__price)
item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40, 34.95)
item3 = RetailItem('Shirt', 20, 24.95)


class CashRegister:
    def __init__(self):
        self.__total = 0
        self.__item_list = []
    def purchase_item(self, item):
        self.__item_list.append(item)
    def get_total(self):
        for x in self.__item_list:
            self.__total += x.get_price()
        return 'Total price of items is: ' + str(self.__total)
    def show_items(self):
        if len(self.__item_list) == 0:
            print('NO item in the list.')
        else:
            print('')
            print('Items selected include: ')
            for x in self.__item_list:
                print(x.get_description())
            print('')
    def clear(self):
        self.__item_list = []


# Demonstrating the Cashregister class
cash = CashRegister()
cash.purchase_item(item1)
cash.purchase_item(item2)
print(cash.get_total())
cash.show_items()

# 9
class Question:
    def __init__(self, question, choice_1, choice_2, choice_3, choice_4, real_answer):
        self.__answer_1 = choice_1
        self.__answer_2 = choice_2
        self.__answer_3 = choice_3
        self.__answer_4 = choice_4
        self.__question = question
        self.__real_answer = real_answer
    def get_question(self):
        return self.__question
    def get_choices(self):
        return 'A--' + self.__answer_1 + \
               '\nB--' + self.__answer_2 + \
               '\nC--' + self.__answer_3 + \
               '\nD--' + self.__answer_4 
    def get_correct_answer(self):
        return self.__real_answer
    def set_choice_1(self, choice_1):
        self.__answer_1 = choice_1
    def set_choice_2(self, choice_2):
        self.__answer_2 = choice_2
    def set_choice_3(self, choice_3):
        self.__answer_3 = choice_3
    def set_choice_4(self, choice_4):
        self.__answer_4 = choice_4
    def set_correct_answer(self,real_answer):
        self.__real_answer = real_answer
question_list = []
question1 = Question('Physical devices a computer is made of are called: ', 'Hardware', 'software', 'operating system', 'tools', 'A')
question2 = Question('Part of a computer that runs a program is called: ', 'RAM', 'CPU', 'Secondary Storage', 'Main memory', 'B')
question3 = Question('Today, CPUs are small chips known as: ', 'ENIACs', 'Microprocessors', 'Memory chips', 'Operating systems', 'B')
question4 = Question('A video display is an ________ device: ', 'input', 'output', 'secondary storage', 'main memory', 'A')
question5 = Question('A byte is made up of _______ bits: ', '4', '12', '16', '8', 'D')
question6 = Question('Bit that is turned off represents______: ', '1', '-1', '0', 'no', 'C')
question7 = Question('Real numbers are encoded using the _________ technique: ', 'two\'s complement', 'unicode', 'ASCII', 'floating point', 'D')
question8 = Question('Negative numbers are encoded using the _________ technique: ', 'two\'s complement', 'unicode', 'ASCII', 'floating point', 'A')
question9 = Question('Computers can only execute programs that are written in ________. ', 'Java', 'Python', 'Machine Language', 'Assembly Language', 'C')
question10 = Question('The rules that must be followed when writting a program are called: ', 'syntax', 'punctuation', 'grammar', 'key-word', 'A')
question_list.append(question1)
question_list.append(question2)
question_list.append(question3)
question_list.append(question4)
question_list.append(question5)
question_list.append(question6)
question_list.append(question7)
question_list.append(question8)
question_list.append(question9)
question_list.append(question10)
y = 1
correct_player1 = 0
correct_player2 = 0
for x in question_list:
    if y % 2 == 0:
        print('This question is for Player 2.')
        print(x.get_question())
        print(x.get_choices())
        answer = input('Please enter the letter of your answer here: ')
        print('')
        if answer.lower() == x.get_correct_answer().lower():
            correct_player2 += 1
        y += 1
    else:
        print('This question is for Player 1.')
        print(x.get_question())
        print(x.get_choices())
        answer = input('Please enter the letter of your answer here: ')
        print('')
        if answer.lower() == x.get_correct_answer().lower():
            correct_player1 += 1
        y += 1
print('')
if correct_player1 > correct_player2:
    print(f'Player 1 won {correct_player1} points')
    print(f'Player 2 won {correct_player2} points')
    print('________________________')
    print('Player 1 won the game.')
elif correct_player2 > correct_player1:
    print(f'Player 1 won {correct_player1} points')
    print(f'Player 2 won {correct_player2} points')
    print('________________________')
    print('Player 2 won the game.')
elif correct_player1 == correct_player2:
    print(f'Player 1 won {correct_player1} points')
    print(f'Player 2 won {correct_player2} points')
    print('________________________')
    print('The game was a tie.')   
          