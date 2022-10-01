# 1
def converter():
    kilometers = float(input('Please enter the kilometers.'))
    miles = kilometers * 0.6214

# 2
def repeat(string_2):
    accumulate = ''
    for j in range(3):
        accumulate = accumulate + string_2

# 3
def insurance(num_2):
    minimum = num_2*0.8
    print('The minimum amount of insurance you should buy is', minimum)

# 4
def total_expenses():
    car = int(input('Please enter your expenses from automobile service. '))
    loan = int(input('Please enter payment you paid for the loan. '))
    insurance_2 = int(input('Please enter your insurance payment. '))
    gas = int(input('Please enter your payment for gas. '))
    oil = int(input('Please enter your payment for the oil. '))
    tires = int(input('Please enter your payment for the tires. '))
    maintenance = int(input('Please enter your payment for maintenance. '))
    total = car + loan + insurance_2 + gas + oil + tires + maintenance
    annual_total = total * 12
    print('Total expenses for the month is', total)
    print('Total expenses for the year is', annual_total)

# 5
def property_tax():
    real_value = int(input('Please enter actual value of your property. '))
    assessment_value = real_value * 0.6
    tax = assessment_value * 0.0072
    print('The assessment value of your land will be', assessment_value)
    print('The tax for your land will be', format(tax, ',.2f'))

# 6
def calories_from_food():
    carbohydrate = int(input('Please enter the grams of carbohydrate consumed in the day. '))
    fat = int(input('Please enter the grams of fat consumed for the day'))
    carbohydrate = carbohydrate * 4
    fat = fat * 9
    print('The total amount of calories consumed from fat is', fat)
    print('The total amount of calories consumed from carbohydrate is', carbohydrate)

# 7
def stadium_seating():
    class_a = int(input('Please enter the number of seats sold for class A: '))
    class_b = int(input('Please enter the number of seats fold for class B: '))
    class_c = int(input('Please enter the number of seats fold for class C: '))
    total_seat = (class_a*20) + (class_b*15) + (class_c*10)
    print('Total income generated from the total seats sold is', total_seat)

# 8
def paint_job():
    wall_space = float(input('Please enter the square feet of wall space to be painted: '))
    price_per_gallon = float(input('Please enter the price per gallon: '))
    gallons_required = wall_space/112
    paint_price = price_per_gallon * gallons_required
    hours = wall_space/14
    labour_charge = hours * 35
    total_cost = labour_charge + paint_price
    print('The number of gallons of paint required is', format(gallons_required, ',.2f'))
    print('The hours of labor required is', format(hours, ',.2f'))
    print('The cost of the paint is', format(paint_price, ',.2f'))
    print('The total labor charge is', format(labour_charge, ',.2f'))
    print('The total cost of the paint job is', format(total_cost, ',.2f'))

# 9
def total_monthly_tax():
    total_sales = float(input('Please enter the total sales of the month: '))
    county_tax = total_sales * 0.025
    state_tax = total_sales * 0.05
    total_tax = county_tax + state_tax
    print('The total county sales tax is', format(county_tax, ',.2f'))
    print('The total state sales tax is', format(state_tax, ',.2f'))
    print('The total sales tax is ', format(total_tax, ',.2f'))

# 10
def feet_to_inches(feet):
    return feet*12
feet_2 = int(input('Please enter the number of feets. '))
print('Total number of inches is', feet_to_inches(feet_2))

# 11
def addition_test():
    import random
    for k in range(1, 6, 1):
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        print('Question', k)
        print(num_1, '+', num_2, '= _______')

# 12
def maximum(int_1, int_2):
    if int_1 >= int_2:
        greater = int_1
    else:
        greater = int_2
    return greater
print(maximum(15, 11))

# 13
def falling_distance(time):
    distance = 0.5*9.8*time*time
    return distance
for i in range(1, 11, 1):
    print(format(falling_distance(i), ',.2f'))

# 14
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity * velocity
mass_2 = float(input('Please enter the mass of the object: '))
velocity_2 = float(input('Please enter the velocity of the object: '))
kinetic_energy(mass_2, velocity_2)

# 15
def calc_average(test_1, test_2, test_3, test_4, test_5):
    sum_average = (test_1 + test_2 + test_3 + test_4 + test_5)/5
    return sum_average


def determine_grade(test_score):
    grade = ''
    if test_score >= 90 and test_score <= 100:
        grade = 'A'
    elif test_score >= 80 and test_score <= 89:
        grade = 'B'
    elif test_score >= 70 and test_score <= 79:
        grade = 'C'
    elif test_score >= 60 and test_score <= 69:
        grade = 'D'
    elif test_score < 60:
        grade = 'F'
    else:
        print('Invalid input. ')
    return grade


# 16
def is_even(num_3):
    flag_2 = True
    if num_3 % 2 == 0:
        flag_2 = True
    else:
        flag_2 = False
    return flag_2
even_counter = 0
odd_counter = 0
import random
for l in range(100):
    number = random.randint(1, 100)
    if is_even(number) == True:
        even_counter += 1
    else:
        odd_counter += 1
print('There were', even_counter, 'even numbers.')
print('There were', odd_counter, 'odd numbers.')

# 17
def is_prime(number_3):
    counter = 0
    for m in range(number_3, 0, -1):
        if number_3 % m == 0:
            counter += 1
    if counter == 2:
        flag_3 = True
    else:
        flag_3 = False
    return flag_3
number_2 = int(input('Please enter some number: '))
if is_prime(number_2) == False:
    print('The number is not a Prime number. ')
else:
    print('The number is a Prime number. ')

# 18
for n in range(1, 101, 1):
    if is_prime(n) == True:
        print(n)

# 19
total_loan = float(input('Please enter the amount of loan you took: '))
monthly_rate = float(input('Please enter the interest rate as a percentage: '))/100
months = int(input('Please enter the number of months you would like to pay back in: '))
def loan_payment_calculator(total_loan_2, monthly_rate_2, months_2):
    num2 = (1+monthly_rate_2)**-months_2
    num3 = 1 - num2
    num4 = monthly_rate_2 * total_loan_2
    payment_per_month = num4/num3
    return payment_per_month
print('The amount of number you have to pay per month will be')
print(format(loan_payment_calculator(total_loan, monthly_rate, months), ',.2f'))

# 20
answer = 'y'
while answer == 'y' or answer == 'Y':
    guess = int(input('Please guess the number: '))
    import random
    random_number = random.randint(1, 101)
    flag_4 = False
    while flag_4 != True:
        if guess > random_number:
            print('Too high, try again.')
            guess = int(input('Please guess the number: '))
        elif guess == random_number:
            print('')  # added for the aesthetic value
            print('Congratulation you guessed the number correctly.')
            print('')  # added for the aesthetic value
            flag_4 = True
        else:
            print('Too low, try again.')
            guess = int(input('Please guess the number: '))
    answer = input('Please enter "y" if you wish to play again. ')

# 21
def rock_paper_scissor():
    import random
    computer_choice = random.randint(1, 4)
    computer_game_choice = 'rock'
    print('What are you a "rock", "paper", or "scissor" ?')
    player_choice = input('Please enter all with a lower case letters: ')
    if computer_choice == 1:
        computer_game_choice = 'rock'
    if computer_choice == 2:
        computer_game_choice = 'paper'
    if computer_choice == 3:
        computer_game_choice = 'scissors'

    if player_choice == computer_game_choice:
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('The game was a draw, Play again.')
        rock_paper_scissor()
    if computer_choice == 2 and player_choice == 'rock':
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Scissors cuts paper.')
        print('Computer wins.')
    if player_choice == 'paper' and computer_choice == 3:
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Scissors cuts paper.')
        print('Computer wins.')
    if player_choice == 'paper' and computer_choice == 1:
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Paper wraps rock.')
        print('Player wins.')
    if computer_choice == 1 and player_choice == 'scissor':
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Rock smashes scissor.')
        print('Computer wins')
    if computer_choice == 2 and player_choice == 'scissor':
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Scissor cuts paper.')
        print('Player wins')
    if computer_choice == 3 and player_choice == 'rock':
        print("Computer's choice is", computer_game_choice)
        print("Player's choice is", player_choice)
        print('Rock smashes scissor.')
        print('Player wins')

# 22
def triangle(x1, x2, x3, y1, y2, y3, color):
    import turtle
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()
triangle(0, 120, 150, 0, 110, 40, 'red')

# 23
import turtle
def drawBase():
    turtle.penup()
    turtle.goto(50, -200)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
def drawMidSection():
    turtle.penup()
    turtle.goto(50, 0)
    turtle.pendown()
    turtle.circle(70)
    turtle.penup()
def drawArms():
    turtle.goto(-20, 70)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(50)
    turtle.setheading(120)
    turtle.forward(40)
    turtle.setheading(75)
    turtle.forward(10)
    turtle.penup()
    turtle.goto(-83.3, 129.64)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(10)
    turtle.penup()
    turtle.goto(120, 70)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(50)
    turtle.setheading(70)
    turtle.forward(15)
    turtle.penup()
    turtle.goto(155.36, 105.36)
    turtle.setheading(340)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
def drawHead():
    turtle.penup()
    turtle.goto(50, 140)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(45)
    turtle.penup()
    turtle.goto(35, 190)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(5)
    turtle.penup()
    turtle.goto(65, 190)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(5)
    turtle.penup()
    turtle.goto(30, 170)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(40)
    turtle.hideturtle()
    turtle.penup()

def drawHat():
    turtle.penup()
    turtle.goto(50, 210)
    turtle.pendown()
    turtle.setheading(180)
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.forward(70)
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(0)
    turtle.forward(30)
    turtle.setheading(90)
    turtle.forward(45)
    turtle.setheading(0)
    turtle.forward(80)
    turtle.setheading(270)
    turtle.forward(45)
    turtle.setheading(0)
    turtle.forward(30)
    turtle.setheading(270)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(70)
    turtle.end_fill()
    turtle.penup()
def main():
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
# 24
import turtle
def drawPattern(height, width):
    half_height = height / 2
    half_width = width / 2
    quarter_height = height / 4
    quarter_width = width / 4
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width, quarter_height)
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.forward(half_width)
    turtle.setheading(90)
    turtle.forward(half_height)
    turtle.setheading(180)
    turtle.forward(half_width)
    turtle.setheading(270)
    turtle.forward(half_height)
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + (quarter_width/2), (quarter_height/2))
    turtle.pendown()
    turtle.forward(half_width + quarter_width)
    turtle.setheading(90)
    turtle.forward(half_height + quarter_height)
    turtle.setheading(180)
    turtle.forward(half_width + quarter_width)
    turtle.setheading(270)
    turtle.forward(half_height + quarter_height)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width, quarter_height)
    turtle.pendown()
    turtle.goto(-100, 0)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width + half_width, quarter_height)
    turtle.pendown()
    turtle.goto(-100 + width, 0)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width + half_width, quarter_height + half_height)
    turtle.pendown()
    turtle.goto(-100 + width, height)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width, half_height + quarter_height)
    turtle.pendown()
    turtle.goto(-100, height)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width, half_height)
    turtle.pendown()
    turtle.goto(-100, half_height)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-100 + quarter_width + half_width, half_height)
    turtle.pendown()
    turtle.goto(-100 + width, half_height)

height_2 = int(input('Please enter the height of the Rectangle: '))
width_2 = int(input('Please enter the width of the Rectangle: '))
drawPattern(height_2, width_2)

# 25
import turtle
def singlesquare(size):
    turtle.hideturtle()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.forward(size)
    for i in range(3):
        turtle.left(90)
        turtle.forward(size)
    turtle.end_fill()
def outer_squares(size):
    for j in range(0, (5 * size) + 1, 2 * size):
        for k in range(0, (5 * size) + 1, 2 * size):
            turtle.penup()
            turtle.goto(k, j)
            turtle.pendown()
            singlesquare(size)
def inner_squares(size):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(size, size)
    turtle.pendown()
    for j in range(size, (3 * size) + 1, 2 * size):
        for k in range(size, (3 * size) + 1, 2 * size):
            turtle.penup()
            turtle.goto(k, j)
            turtle.pendown()
            singlesquare(size)
def outer_boundary(size):
    turtle.hideturtle()
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.forward(size * 5)
    for i in range(3):
        turtle.left(90)
        turtle.forward(size * 5)
def checkboard(size):
    outer_squares(size)
    inner_squares(size)
    outer_boundary(size)
# 26
import turtle
import random
def drawBuiling():
    turtle.hideturtle()
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('gray')
    turtle.goto(0, 100)
    turtle.goto(35, 100)
    turtle.goto(35, 150)
    turtle.goto(80, 150)
    turtle.goto(80, 250)
    turtle.goto(150, 250)
    turtle.goto(150, 140)
    turtle.goto(200, 140)
    turtle.goto(200, 200)
    turtle.goto(240, 200)
    turtle.goto(240, 150)
    turtle.goto(270, 150)
    turtle.goto(270, 100)
    turtle.goto(300, 100)
    turtle.goto(300, 0)
    turtle.goto(0, 0)
    turtle.end_fill()
def drawSky():
    turtle.hideturtle()
    turtle.pencolor('black')
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.penup()
    turtle.goto(300, 100)
    turtle.pendown()
    turtle.goto(300, 300)
    turtle.goto(0, 300)
    turtle.goto(0, 100)
    turtle.goto(35, 100)
    turtle.goto(35, 150)
    turtle.goto(80, 150)
    turtle.goto(80, 150)
    turtle.goto(80, 250)
    turtle.goto(150, 250)
    turtle.goto(150, 140)
    turtle.goto(200, 140)
    turtle.goto(200, 200)
    turtle.goto(240, 200)
    turtle.goto(240, 150)
    turtle.goto(270, 150)
    turtle.goto(270, 100)
    turtle.goto(300, 100)
    turtle.end_fill()
def drawStars():
    turtle.hideturtle()
    turtle.pencolor('white')
    for i in range(3):
        x1 = random.randint(0, 81)
        y1 = random.randint(150, 300)
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.dot()
    x1 = random.randint(80, 151)
    y1 = random.randint(250, 300)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pencolor('white')
    turtle.dot()
    for i in range(3):
        x1 = random.randint(150, 301)
        y1 = random.randint(200, 301)
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pencolor('white')
        turtle.dot()
def drawsingleWindow(x5, y5):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x5, y5)
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.fillcolor('white')
    turtle.pencolor('white')
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.end_fill()
def drawAllwindows():
    drawsingleWindow(60, 125)
    drawsingleWindow(90, 180)
    drawsingleWindow(90, 200)
    drawsingleWindow(110, 70)
    drawsingleWindow(130, 140)
    drawsingleWindow(220, 180)
def cityskyline():
    drawBuiling()
    drawSky()
    drawAllwindows()
    drawStars()
cityskyline()
