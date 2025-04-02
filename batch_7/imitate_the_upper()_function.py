#imitate upper() function without using upper()

"""
This function takes a string as input and returns the string
with all characters converted to uppercase letters.
"""

def imitate_upper(string):
    result = []
    for i in string:
        if 'a' <= i <= 'z':
            result.append(chr(ord(i) - 32))
        else:
            result.append(i)
    return ''.join(result)


print(imitate_upper("Hello World"))