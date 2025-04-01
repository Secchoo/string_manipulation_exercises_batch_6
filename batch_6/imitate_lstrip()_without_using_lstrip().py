#to remove starting spaces from a string
# without using lstrip() method.

"""
This function removes leading spaces from a string
"""

def custom_lstrip(string):
    start = 0
    # Loop until a non-whitespace character is found
    while start < len(string) and string[start].isspace():
        start += 1
    return string[start:]

#print the result
print(custom_lstrip("   Hello World!   "))