#To check if string is upper case or not without using isupper() method

"""
this function checks if a string is upper case or not
without using the built-in isupper() method.
"""

def is_upper(string):
    has_cased = False
    all_upper = True
    for i in string:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            has_cased = True
            if 'a' <= i <= 'z':
                all_upper = False
    return has_cased and all_upper

print(is_upper("HELLO WORLD"))  # True
print(is_upper("Hello World"))  # False


