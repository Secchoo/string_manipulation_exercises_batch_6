# Imitate rstrip() function without using rstrip()

"""
This function takes a string as input and returns the string 
with trailing whitespace removed.
"""

def imitate_rstrip(string):
    end = len(string)  # Start from the end of the string
    while end > 0 and string[end - 1] == ' ':  # Check for trailing spaces
        end -= 1  # Move the end pointer backward for each trailing space
    return string[:end]  # Return the string up to the last non-space character



print(imitate_rstrip("Hello World    "))  