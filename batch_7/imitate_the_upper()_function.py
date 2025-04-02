# Imitate upper() function without using upper()

"""
This function takes a string as input and returns the string
with all characters converted to uppercase letters.
"""

def imitate_upper(string):
    result = []  # Initialize an empty list to store the converted characters
    for i in string:
        if 'a' <= i <= 'z':  # Check if the character is a lowercase letter
            result.append(chr(ord(i) - 32))  # Convert to uppercase using ASCII values
        else:
            result.append(i)  # Append the character as is if it's not lowercase
    return ''.join(result)  # Join the list into a single string and return it



print(imitate_upper("Hello World"))  