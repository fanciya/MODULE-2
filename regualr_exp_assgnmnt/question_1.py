# 1. Write a Python program that matches a string 
# that has an a followed by zero or more b's.

import re
def match_pattern(text):
    pattern = r'ab*'  
    if re.match(pattern, text):
        return True
    else:
        return False
input_string = input("Enter a string: ")
if match_pattern(input_string):
    print("Match found!")
else:
    print("No match found.")



# 2.Write a Python program to check that a string contains 
# only a certain set of characters (in this case a-z, A-Z and 0-9).

# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9]')
#     string = charRe.search(string)
#     return not bool(string)

# print(is_allowed_specific_char("ABCDEFabcdef123450")) 
# print(is_allowed_specific_char("*&%@#!}{"))
