#imitate upper() function without using upper()

"""
This function takes a string as input and returns the string
with all characters converted to uppercase letters.
"""

def custom_upper(s):
    result = []
    for c in s:
        if 'a' <= c <= 'z':
            result.append(chr(ord(c) - 32))
        else:
            result.append(c)
    return ''.join(result)


print(custom_upper("Hello World"))