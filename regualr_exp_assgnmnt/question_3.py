# 3.Write a Python program to find sequences of lowercase letters joined with  an underscore.

import re
def find_sequences_with_underscore(input_string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences
input_string = input("Enter a string: ")
result = find_sequences_with_underscore(input_string)
if result:
    print("Sequences of lowercase letters joined with an underscore found:")
    print(result)
else:
    print("No sequences of lowercase letters joined with an underscore found in the input string.")
