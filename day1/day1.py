## Part 1

import re

def get_two_digit_number(string):
    digits_list = re.findall(r'\d',string)
    number = int(digits_list[0]) * 10 + int(digits_list[-1])
    return(number)   


def get_number_per_line(file_name):
    with open(file_name) as f:
        number_list = [get_two_digit_number(line) for line in f]
        number_list_sum = sum(number_list)
        print(number_list_sum)

file_name = "input.txt"
get_number_per_line(file_name)

## Part 2

str_to_int_dict = {'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9}

def str_to_int(val):
    return val if val.isdigit() else str_to_int_dict[val]

def get_two_digit_number_str(string):
    print(string)
    # the positive lookahead (?=...) checks for a match, but doesn’t consume any of the string. This means that after the lookahead has been evaluated, the regex engine hasn't moved on the string being parsed.
    # If we don't put it, ant two numbers share letters (e.g. twone), it will only capture the two, and not two and one 
    regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))'
    digits_list = re.findall(regex,string)
    print(digits_list)
    number = int(str_to_int(digits_list[0])) * 10 + int(str_to_int(digits_list[-1]))
    print(number)
    return(number)   

def get_number_per_line2(file_name):
    with open(file_name) as f:
        number_list = [get_two_digit_number_str(line) for line in f]
        number_list_sum = sum(number_list)
        print(number_list_sum)

file_name = "input.txt"
get_number_per_line2(file_name)

