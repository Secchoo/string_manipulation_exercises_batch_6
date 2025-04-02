# Imitate startswith() function without using startswith()

"""
This function checks if a string starts with a given prefix.
It returns True if it does, and False otherwise.
"""

def imitate_startswith(string, prefix):
    # Check if the prefix is longer than the string
    if len(prefix) > len(string):
        return False  # A longer prefix cannot match the start of the string
    # Compare the start of the string with the prefix
    return string[:len(prefix)] == prefix



print(imitate_startswith("HelloWorld", "Hello"))  