#to remove prefix from a string 

"""
This function removes a specified prefix
from a string without using the built-in removeprefix() method.
"""


def custom_removeprefix(string, prefix):
    # Check if the prefix is empty
    if len(prefix) == 0:
        return string
    # Check if the string starts with the prefix
    if len(string) >= len(prefix) and string[:len(prefix)] == prefix:
        return string[len(prefix):]
    return string

#print the result
print(custom_removeprefix("HelloWorld", "Hello"))