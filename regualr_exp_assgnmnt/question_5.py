# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


import re
def match_pattern(input_string):
    pattern = r'^a.*b$' 
    if re.match(pattern, input_string):
        return True
    else:
        return False
input_string = input("Enter a string: ")

if match_pattern(input_string):
    print("Input string matches the pattern: 'a' followed by anything, ending in 'b'.")
else:
    print("Input string does not match the pattern.")
