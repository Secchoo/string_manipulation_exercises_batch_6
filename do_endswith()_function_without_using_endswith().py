#To check if the end of a string ends with a given suffix or 
#not without using endswith() method.

"""
This function checks if a string ends with a given 
suffix without using the built-in endswith() method.
"""

# endswith() function without using endswith()
def endswith(string, suffix):
    if len(suffix) == 0:
        return True
    if len(string) < len(suffix):
        return False
    return string[-len(suffix):] == suffix

#prints the result
print(endswith("hello world", "world"))  
print(endswith("hello world", "hello"))