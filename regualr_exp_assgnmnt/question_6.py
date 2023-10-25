#  A website requires the users to input username and password to register.         Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12


import re
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"
    if re.match(pattern, password):
        return True
    else:
        return False
password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid. Please make sure it meets the specified criteria.")
