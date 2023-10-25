# 4.Write a python program that matches a 
# string only contain 0-9 as the characters and it must be at least 1 char in length and no more than 6.

import re

def validate_input(input_string):
    
    pattern = r'^[0-9]{1,6}$'
    if re.match(pattern, input_string):
        return True
    else:
        return False
input_string = input("Enter a string (only digits 0-9, 1 to 6 characters): ")
if validate_input(input_string):
    print("Input string is valid.")
else:
    print("Input string is not valid. It should contain only digits 0-9, 1 to 6 characters.")
