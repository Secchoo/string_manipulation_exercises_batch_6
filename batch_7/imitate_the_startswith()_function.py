#imitate startswith() function without using startswith()

"""
This function checks if a string starts with a given prefix.
It returns True if it does, and False otherwise.
"""

def imitate_startswith(string, prefix):
    if len(prefix) > len(string):
        return False
    return string[:len(prefix)] == prefix


print(imitate_startswith("HelloWorld", "Hello"))