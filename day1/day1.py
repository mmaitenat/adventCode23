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
