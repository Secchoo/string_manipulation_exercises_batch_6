#To check if string is upper case or not without using isupper() method

"""
this function checks if a string is upper case or not
without using the built-in isupper() method.
"""

def is_upper(s):
    has_cased = False
    all_upper = True
    for c in s:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            has_cased = True
            if 'a' <= c <= 'z':
                all_upper = False
    return has_cased and all_upper

print(is_upper("HELLO WORLD"))  # True
print(is_upper("Hello World"))  # False


