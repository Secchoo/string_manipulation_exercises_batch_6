#to remove starting spaces from a string
# without using lstrip() method.

"""
This function removes leading spaces from a string
"""

def custom_lstrip(s):
    start = 0
    # Loop until a non-whitespace character is found
    while start < len(s) and s[start].isspace():
        start += 1
    return s[start:]

#print the result
print(custom_lstrip("   Hello World!   "))