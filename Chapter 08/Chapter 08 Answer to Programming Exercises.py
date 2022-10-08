# 1
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
initials = (first_name[0]+'.').upper() + (last_name[0]+'.').upper()
name_in_book = first_name + ' ' + last_name.upper()
user_name = first_name[0].lower() + last_name.lower()
print('Initials -->', initials)
print('Name in address book-->', name_in_book)
print('Username --> ', user_name)

# 2
def sum_finder(digits):
    counter = 0
    for i in digits:
        counter += int(i)
    return counter
print(sum_finder('2514'))
# The code in the above line will display 12

# 3
def date_printer(date_string):
    new_list = date_string.split('/')
    date = new_list[1]
    month = int(new_list[0])
    year = new_list[2]
    if month == 1:
        month_name = 'January'
    elif month == 2:
        month_name = 'February'
    elif month == 3:
        month_name = 'March'
    elif month == 4:
        month_name = 'April'
    elif month == 5:
        month_name = 'May'
    elif month == 6:
        month_name = 'June'
    elif month == 7:
        month_name = 'July'
    elif month == 8:
        month_name = 'August'
    elif month == 9:
        month_name = 'September'
    elif month == 10:
        month_name = 'October'
    elif month == 11:
        month_name = 'November'
    elif month == 12:
        month_name = 'December'
    else:
        month_name = "Can't find the name. "
    print(month_name+' ' + date + ',' + year)
date_printer('10/12/1994') # This is for testing the program.

# 4
def morse_convertor(morse_code):
    morse_code = morse_code.upper()
    converted_code = ''
    for i in morse_code:
        if i == ' ':
            converted_code += ' '
        elif i == ',':
            converted_code += '--..--'
        elif i == '.':
            converted_code += '.-.-.-'
        elif i == '?':
            converted_code += '..--..'
        elif i == '0':
            converted_code += '-----'
        elif i == '1':
            converted_code += '.----'
        elif i == '2':
            converted_code += '..---'
        elif i == '3':
            converted_code += '...--'
        elif i == '4':
            converted_code += '....-'
        elif i == '5':
            converted_code += '.....'
        elif i == '6':
            converted_code += '-....'
        elif i == '7':
            converted_code += '--...'
        elif i == '8':
            converted_code += '---..'
        elif i == '9':
            converted_code += '----.'
        elif i == 'A':
            converted_code += '.-'
        elif i == 'B':
            converted_code += '-...'
        elif i == 'C':
            converted_code += '-.-.'
        elif i == 'D':
            converted_code += '-..'
        elif i == 'E':
            converted_code += '.'
        elif i == 'F':
            converted_code += '..-.'
        elif i == 'G':
            converted_code += '--.'
        elif i == 'H':
            converted_code += '....'
        elif i == 'I':
            converted_code += '..'
        elif i == 'J':
            converted_code += '.---'
        elif i == 'K':
            converted_code += '-.-'
        elif i == 'L':
            converted_code += '.-..'
        elif i == 'M':
            converted_code += '--'
        elif i == 'N':
            converted_code += '-.'
        elif i == 'O':
            converted_code += '---'
        elif i == 'P':
            converted_code += '.--.'
        elif i == 'Q':
            converted_code += '--.-'
        elif i == 'R':
            converted_code += '.-.'
        elif i == 'S':
            converted_code += '...'
        elif i == 'T':
            converted_code += '-'
        elif i == 'U':
            converted_code += '..-'
        elif i == 'V':
            converted_code += '...-'
        elif i == 'W':
            converted_code += '.--'
        elif i == 'X':
            converted_code += '-..-'
        elif i == 'Y':
            converted_code += '-.-'
        elif i == 'Z':
            converted_code += '--..'
        else:
            converted_code += ' '
    return converted_code
print(morse_convertor('how are you')) # This is a sample input

# 5
def Telephone_number_converter(number):
    number_list = number.split('-')
    new_number = ''
    first_set = number_list[0]
    second_set = number_list[1].upper()
    third_set = number_list[2].upper()
    new_number += first_set
    new_number += '-'
    for i in second_set:
        if i == 'A' or i == 'B' or i == 'C':
            new_number += '2'
        elif i == 'D' or i == 'E' or i == 'F':
            new_number += '3'
        elif i == 'G' or i == 'H' or i == 'I':
            new_number += '4'
        elif i == 'J' or i == 'K' or i == 'L':
            new_number += '5'
        elif i == 'M' or i == 'N' or i == 'O':
            new_number += '6'
        elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
            new_number += '7'
        elif i == 'T' or i == 'U' or i == 'V':
            new_number += '8'
        elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            new_number += '9'
    new_number += '-'
    for i in third_set:
        if i == 'A' or i == 'B' or i == 'C':
            new_number += '2'
        elif i == 'D' or i == 'E' or i == 'F':
            new_number += '3'
        elif i == 'G' or i == 'H' or i == 'I':
            new_number += '4'
        elif i == 'J' or i == 'K' or i == 'L':
            new_number += '5'
        elif i == 'M' or i == 'N' or i == 'O':
            new_number += '6'
        elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
            new_number += '7'
        elif i == 'T' or i == 'U' or i == 'V':
            new_number += '8'
        elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            new_number += '9'
    return new_number
print(Telephone_number_converter('555-get-food')) # This is a sample input.

# 6
def average_word_in_text(text_name):
    text_file = open(text_name, 'r')
    text_list = text_file.readlines()
    i = 0
    while i < len(text_list):
        text_list[i] = text_list[i].rstrip('\n')
        i += 1
    accumulator_1 = 0
    accumulator_2 = 0
    for j in text_list:
        new_list = j.split()
        accumulator_2 += 1  # keeps track of the number of sentences
        for k in new_list:
            accumulator_1 += len(k)  # keeps track of number of words in sentence.
    return accumulator_1 / accumulator_2
print(average_word_in_text('text.txt')) # This is a sample example.

# 7
def text_analyser(text_name):
    text_file = open(text_name, 'r')
    text_list = text_file.readlines()
    i = 0
    lines = 0
    upper_case = 0
    lower_case = 0
    digits = 0
    whitespace = 0
    while i < len(text_list):
        text_list[i] = text_list[i].rstrip('\n')
        i += 1
    for l in text_list:
        lines += 1
        new_list = l.split()
        for s in new_list:
            for k in s:
                if k.isupper():
                    upper_case += 1
                if k.islower():
                    lower_case += 1
                if k.isdigit():
                    digits += 1
            whitespace += 1
    return [upper_case, lower_case, digits, whitespace-lines]
analyisis_list = text_analyser('text.txt')
print('The number of uppercase letters in the file is', analyisis_list[0])
print('The number of lowercase letters in the file is', analyisis_list[1])
print('The number of digits in the file is', analyisis_list[2])
print('The number of whitespace characters in the file is', analyisis_list[3])

# 8
def sentence_capitalizer(sentence):
    new_list = sentence.split('.')
    updated_list = []
    i = 0
    while i < len(new_list):
        new_list[i] = new_list[i].strip()
        i += 1
    for i in new_list:
        flag = False
        new_word = ''
        for u in i:
            if flag is False:
                new_word += u.upper()
                flag = True
            else:
                new_word += u
        updated_list.append(new_word)
    capitalized_sent = ''
    for i in updated_list:
        capitalized_sent += i + ' '
    print(capitalized_sent)
sentence_capitalizer('hello. my name is Joe. what is your name?')
# The above code examples a sample sentence

# 9
def vowels(string_2):
    vowels = 0
    for i in string_2:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1
    return vowels
def consonants(string_2):
    length = len(string_2)
    consonants = 0
    for i in string_2:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            consonants += 0
        else:
            consonants += 1
    return consonants
the_string = input('Please enter the string to be analysed: ')
print('The total number of vowels in this word is', vowels(the_string))
print('The total number of consonants in this word is', consonants(the_string))

# 10
the_another_string = input('Please enter the word: ')
string = []
repition = []
new_string = ''
for i in the_another_string:
    string.append(i)
for i in the_another_string:
    repition.append(0)
y = 0 # This is a counter for the index of each character
x = 1 # This is a counter for the repetition of each character
for i in string:
    if i in new_string:
        x += 1
        repition[y] += x
        y += 1
        new_string += i
    else:
        x = 1
        repition[y] += x
        y += 1
        new_string += i
print(repition)
maximum = max(repition)
max_index = repition.index(maximum)
repeated = string[max_index]
print(repeated)

# 11
def word_separator(the_word):
    new_word = ''
    flag = False
    for i in the_word:
        if i.isupper() and flag is False:
            new_word += " " + i
            flag = True
        elif i.isupper() and flag is True:
            new_word += " " + i.lower()
        else:
            new_word += i.lower()
    return new_word.strip()
print(word_separator('StopAndSmellTheRoses.')) # This is a sample example

# 12
def pig_latin(the_word):
    new_list = the_word.split()
    pig_list = []
    for i in new_list:
        length = len(i)
        new_i = ''
        new_i += i[1: length]
        new_i += i[0]
        pig_list.append(new_i + 'AY')
    flag = False
    pig_word = ''
    for i in pig_list:
        if flag is False:
            pig_word += i
            flag = True
        else:
            pig_word += ' ' + i
    return pig_word
print(pig_latin('I SLEPT MOST OF THE NIGHT')) # This is a sample example

# 13
def unified_list(num_list):
    master_list = []
    draw_list = []
    for draw in num_list:
        draw_list = draw.split()
        master_list += draw_list
    return master_list, draw_list


def times_each_appears(the_list):
    counter = 0
    numbersfound = []
    timesfound = []

    # Iterate each number in the list.
    for number in the_list:
        if number not in numbersfound:
            # Setup a counter to check how many times a number is seen.
            counter = 0

            # Check how many times the number is in this list.
            for searchnumber in the_list:

                # If the number is found, add + 1 to the counter.
                if number == searchnumber:
                    counter += 1

        if number not in numbersfound:
            numbersfound.append(number)
            timesfound.append(counter)
    return numbersfound, timesfound


def top10common(times, numbers):
    counter = 0
    place = 0
    top10times = []
    top10numbers = []
    for count in range(10):
        # Find the index number of the number that appears the most times.
        place = (times.index(max(times)))
        # Add this number to the list top10numbers
        top10numbers.append(numbers[place])
        # Add the number of times it was found to top10times
        top10times.append(times[place])
        # remove the number from the searchlist
        del numbers[place]
        del times[place]
    print('Most Common Numbers')
    print('-------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for place in range(len(top10numbers)):
        print(top10numbers[place] + '\t--->\t' + str(top10times[place]))
    print()


def bottom10common(times, numbers):
    counter = 0
    place_holder = 0
    bottom10times = []
    bottom10numbers = []
    for count in range(10):
        # Find the index of the number that appear the least times.
        place_holder = times.index(min(times))
        # Add this number to the bottom10numbers
        bottom10numbers.append(numbers[place_holder])
        # Add the number of times it was found to the bottom10times list
        bottom10times.append(times[place_holder])
        # remove the number from the lists times and numbers.
        del numbers[place_holder]
        del times[place_holder]
    print('Least Common Numbers')
    print('--------------------')
    print('Numbers\t\tTimes')
    print('-------\t\t-----')
    for place_holder in range(len(bottom10numbers)):
        print(bottom10numbers[place_holder] + '\t--->\t' + str(bottom10times[place_holder]))
    print()


def top10overdue(times, numbers, original_list):
    counter_3 = 0
    overdue_list = []
    not_seen_list = []
    placeholder = ''
    for number in numbers:
        placeholder = number
        for specific_number in numbers:
            if specific_number == placeholder:
                counter_3 = 0
            else:
                counter_3 += 1
        overdue_list.append(number)
        not_seen_list.append(counter_3)
    top10overdue = []
    top10notseenfor = []
    for counter_3 in range(10):
        index = not_seen_list.index(max(not_seen_list))
        top10notseenfor.append(not_seen_list[index])
        top10overdue.append(overdue_list[index])
        del not_seen_list[index]
        del overdue_list[index]
    print("Overdue List")
    print("------------")
    print()
    print('Number\t\tOverdue')
    print('------\t\t-------')
    for index in range(len(top10overdue)):
        print(top10overdue[index] + '\t--->\t' + str(top10notseenfor[index]))
    print()


def seperate_frequency(a_list):
    powerballs = []
    powerballs_count = []
    non_powerballs = []
    non_powerballs_count = []
    counter_4 = 0
    number = 0
    for count in range(1, 27):
        number = count
        # Split the list into draws
        for draw in a_list:
            draw_list = draw.split()
            if int(draw_list[5]) == number:
                counter_4 += 1
        powerballs.append(number)
        powerballs_count.append(counter_4)
        counter_4 = 0

    for count in range(1, 70):
        number = count
        for draw in a_list:
            draw_list = draw.split()
            for searchnumber in draw_list:
                if int(searchnumber) == number:
                    counter_4 += 1
        non_powerballs.append(number)
        non_powerballs_count.append(counter_4)
        counter_4 = 0

    print('Powerballs Frequency')
    print('--------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(powerballs)):
        print(str(powerballs[index]) + '\t--->\t' + str(powerballs_count[index]))
    print()
    print('Regulars Frequency')
    print('------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(non_powerballs)):
        print(str(non_powerballs[index]) + '\t--->\t' + str(non_powerballs_count[index]))


def main():
    infile = open('pbnumbers.txt', 'r')
    contents = infile.readlines()
    for index in range(len(contents)):
        contents[index] = contents[index].rstrip('\n')
    master_list, split_list = unified_list(contents)
    numbersfound, timesfound = times_each_appears(master_list)

    top10common(timesfound, numbersfound)
    bottom10common(timesfound, numbersfound)
    top10overdue(timesfound, numbersfound, master_list)
    seperate_frequency(contents)
    infile.close()


main()

# 14
def text_to_list(text_here):
    new_text = open(text_here, 'r')
    new_list = new_text.readlines()
    x = 0
    while x < len(new_list):
        new_list[x] = new_list[x].rstrip('\n')
        x += 1
    return new_list


def data_and_time_separator(the_list):
    new_data_list = []
    new_time_list = []
    for price in the_list:
        new_data_list.append(price[11:])
    for time in the_list:
        new_time_list.append(time[0:10])
    data_devided = [new_data_list, new_time_list]
    return data_devided


def average_per_year(the_lists):
    date = the_lists[1]
    print(date)


average_per_year(data_and_time_separator(text_to_list('GasPrices.txt')))

# 15
def ceasar_cipher():
    the_message = input('Please enter the message : ')
    the_digit = int(input('Please enter amount to add in the alphabet : '))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ceasor_word = ''
    while the_digit >= 26:
        the_digit -= 26
    for i in the_message:
        i = i.upper()
        position = alphabet.find(i)
        if position == -1:
            ceasor_word += ' '
        elif position > (26 - the_digit):
            new_position = position + the_digit - 26
            ceasor_word += alphabet[new_position]
        elif position <= (26 - the_digit):
            new_position = position + the_digit
            ceasor_word += alphabet[new_position]
    print(ceasor_word)
ceasar_cipher()
