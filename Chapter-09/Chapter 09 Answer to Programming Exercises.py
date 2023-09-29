#   ------- >>> Answer to Programming Exercises <<< ------- #
# 1
moons_and_radius = {'Io':1821.6, 'Europa':1560.8, 'Ganymede':2634.1, 'Callisto':2410.3}
moons_and_gravity = {'Io':1.796, 'Europa':1.314, 'Ganymede':1.428, 'Callisto':1.235}
moons_and_period = {'Io':1.769, 'Europa':3.551, 'Ganymede':7.154, 'Callisto':16.689}
name = input('Please enter the name of the moon: ')
print(f'The moon\'s mean radius is {moons_and_radius[name]}')
print(f'The moon\'s surface gravity is {moons_and_gravity[name]}')
print(f'The moon\'s orbital period is {moons_and_period[name]}')

# 2
countries_and_capitals = {'Afghanistan':'Kabul', 'Argentina':'Buenos Aires', 'Australia':'Canberra',
                        'Belgium':'Brussels', 'Botswana': 'Gaborone', 'Brazil':'Brasilia', 
                        'Canada':'Ottawa'}
correct = 0
incorrect = 0
response = 'y'
try:
    while response.lower() == 'y':
        question = countries_and_capitals.popitem()
        country = question[0]
        capital = question[1]
        answer = input(f'What is the capital of {country} ?')
        if answer.lower() == capital.lower():
            correct += 1
            print('Congratulations, your answer was correct')
        else:
            incorrect += 1
            print('Sorry, Your answer was not correct.')
        print(f'The number of questions answered correctly is {correct}.')
        print(f'The number of questions answered incorrectly is {incorrect}.')
        response = input('Please enter "y" if you wish to continue. or else if you wish to stop. ')
except KeyError:
    print('All of the countries have been used, Please restart the game.')

# 3
codes = {'h':'u', 'l':'c', 'e':'l', 'o':'j'} # This is a sample dictionary
file_name = input('Please enter the name of the file you want to open: ')
file_here = open(file_name, 'r')
new_list = []
new_list = file_here.readlines()
i = 0
for m in new_list:
    new_list[i] = new_list[i].rstrip('\n')
    i += 1

new_list_2 = []
for m in new_list:
    new_string = ''
    for n in m:
        new_string += codes[n]
    new_list_2.append(new_string)
new_file_2 = open('codedfile.txt', 'w')

for item in new_list_2:
    new_file_2.writelines(item + '\n')

# 4
file_name = input('Please enter the name of the file you want to open: ')
text_file = open(file_name, 'r')
new_list = text_file.readlines()
i = 0
for x in new_list:
    new_list[i] = new_list[i].rstrip('\n')
    i += 1

words_holder = set()
for i in new_list:
    for j in i:
        words_holder.add(j)
print(words_holder)

# 5
import random 
frequencies = {}
for i in range(100):
    num = random.randint(1,10)
    if num in frequencies:
        new_frequency = frequencies[num]
        frequencies[num] = new_frequency + 1
    else:
        frequencies[num] = 1
print(frequencies)

# 6
def set_generator(file_name):
    text_file = open(file_name, 'r')
    new_list = text_file.readlines()
    i = 0
    for x in new_list:
        new_list[i] = new_list[i].rstrip('\n')
        i += 1
    words_holder = set()
    for i in new_list:
        for j in i:
            words_holder.add(j)
    return words_holder
file_name_1 = input('Please enter the name of the file you want to open: ')
file_name_2 = input('Please enter the name of the other file you want to open: ')
set_1 = set_generator(file_name_1)
set_2 = set_generator(file_name_2)
print('A list of unique words contained in the first file is')
print(list(set_1))
print('A list of unique words contained in the second file is')
print(list(set_2))
print('A list of unique words contained in the first but not on the second file is')
print(list(set_1.difference(set_2)))
print('A list of unique words contained in the second but not on the first file is')
print(list(set_2.difference(set_1)))
print('A list of unique words contained in either but not on both is')
print(list(set_2.symmetric_difference(set_1)))

# 7
winners_file = open('WorldSeriesWinners.txt', 'r')
winners_list = winners_file.readlines()
i = 0
for x in winners_list:
    winners_list[i] = winners_list[i].rstrip('\n')
    i += 1

winners_record = {}
i = 1903
for x in winners_list:
    if x == 'World Series Not Played in 1994' or x == 'World Series Not Played in 1904':
        continue
    else:
        if x in winners_record:
            new_record = winners_record[x]
            winners_record[x] = new_record + 1
        if x not in winners_record:
            winners_record[x] = 1


winners_year_record = {}
first_year = 1903
for x in winners_list:
    winners_year_record[first_year] = x
    first_year += 1
    
year = int(input('Please enter the year you like to see who won between 1903-2009: '))
while year < 1903 or year > 2009:
    print('Invalid year. ')
    year = int(input('Please enter the year you like to see who won between 1903-2009: '))

if year == 1904 or year == 1994:
    print('World Series not played in this year.')

else:
    print(f'{winners_year_record[year]} won the World Series that year.')
    print(f'{winners_year_record[year]} has won the World Series {winners_record[winners_year_record[year]]} times')
    print('in the years between 1903 and 2009. ')

# 8
import pickle
print('Good day.')
print('Choice Number \t\t Task')
print('---------------------------------------------------------------')
print('1             \t\t See the list of vegetables.')
print('2             \t\t Add a new vegetable and a price.')
print('3             \t\t Change price of an existing vegetable.')
print('4             \t\t Delete an existing vegetable and price. ')
print('')
choice = int(input('Please enter the number of your choice: '))
vege_dict = {}
if choice == 1:
    vegetables = open('vegetables.dat', 'rb')
    vege_dict = pickle.load(vegetables)
    print(vege_dict)
elif choice == 2:
    vegetables = open('vegetables.dat', 'wb')
    answer = 'y'
    while answer.lower() == 'y':
        print('')
        vegetable_name = input('Please enter the name of the vegetable you like to add: ')
        vegetable_price = input('Please enter the price of the vegetable : ')
        vege_dict[vegetable_name] = vegetable_price
        print('The vegetable name and its price was successfully added.')
        answer = input('Please enter "y" if you wish to continue or else if you wish to stop.')
    pickle.dump(vege_dict, vegetables)
    vegetables.close()
elif choice == 3:
    vegetables = open('vegetables.dat', 'wb')
    answer = 'y'
    while answer.lower() == 'y':
        print('')
        vegetable_name = input('Please enter the name of the vegetable you like to change price: ')
        vegetable_price = input('Please enter the new price of the vegetable: ')
        vege_dict[vegetable_name] = vegetable_price
        print("The vegetable's price was successfully updated.")
        answer = input('Please enter "y" if you wish to continue or else if you wish to stop.')
    pickle.dump(vege_dict, vegetables)
    vegetables.close()
elif choice == 4:
    vegetables = open('vegetables.dat', 'wb')
    answer = 'y'
    while answer.lower() == 'y':
        vegetable_name = input('Please enter the name of the vegetable you like to delete: ')
        del vege_dict[vegetable_name]
        print('The vegetable name and its price was successfully deleted.')
        answer = input('Please enter "y" if you wish to continue or else if you wish to stop.')
    pickle.dump(vege_dict, vegetables)
    vegetables.close()
else:
    print('Invalid Choice.')

# 9
import random
deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
             '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
             '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
             '10 of Spades':10, 'Jack of Spades':10,
             'Queen of Spades':10, 'King of Spades': 10,

             'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
             '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
             '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
             '10 of Hearts':10, 'Jack of Hearts':10,
             'Queen of Hearts':10, 'King of Hearts': 10,

             'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
             '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
             '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
             '10 of Clubs':10, 'Jack of Clubs':10,
             'Queen of Clubs':10, 'King of Clubs': 10,

             'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
             '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
             '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
             '10 of Diamonds':10, 'Jack of Diamonds':10,
             'Queen of Diamonds':10, 'King of Diamonds': 10}



def card_dealer():
    player1 = 0
    player1score = 0
    player2 = 0
    player2score =0
    count = 0
    for i in range(len(deck)//2):
        key = random.choice(list(deck.keys()))
        value = deck[key]
        if deck[key] == 1:
            if player1 + 11 < 21:
                value = 11
            else:
                value = 1
        player1 += value
    

        key = random.choice(list(deck.keys()))
        value = deck[key]

        if deck[key] == 1:
            if player2 + 11 < 21:
                value = 11
            else:
                value = 1
        player2 += value
    
        if player1 > 21 and player2 > 21:
            player1 = 0
            player2 = 0
            print('No body wins')
        elif player1 > 21 and player2 <= 21:
            player1 = 0
            player2 = 0
            player2score += 1
            print('Player 2 wins.')
        elif player2 > 21 and player1 <= 21:
            print('Player 1 wins.')
            player1 = 0
            player2 = 0
            player1score += 1
        else:
            print('The game goes on.')
    print('')
    print('------------GAME\'S RESULT------------' )
    print('')
    if player1score > player2score:
        print('Player 1 wins.')
    elif player2score > player1score:
        print('Player 2 wins.')
    else:
        print('Its a TIE.')
    print('')
           
card_dealer()

# 10
file_name_3 = input('Please enter the name of the file you want to access. ')
text_file = open(file_name_3, 'r')
file_list = text_file.readlines()
i = 0
word_index = {}
for x in file_list:
    file_list[i] = file_list[0].rstrip('\n')
    i += 1
line_number = 1
for line in file_list:
    word_list = line.split()
    for word in word_list:
        if word in word_index:
            new_index = word_index[word]
            new_index = new_index.append(line_number)
            word_index[word] = new_index
        else:
            new_index = 1
            word_index[word] = new_index
print(word_index)
text_file.close()
