#use endwith() function without using endswith() 

"""
This function checks if a string ends with a given 
suffix without using the built-in endswith() method.
"""

def endswith(s, suffix):
    if len(suffix) == 0:
        return True
    if len(s) < len(suffix):
        return False
    return s[-len(suffix):] == suffix

print(endswith("hello world", "world"))  
print(endswith("hello world", "hello"))