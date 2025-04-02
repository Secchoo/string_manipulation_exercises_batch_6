#imitate islower() function without using islower()

"""
This function takes a string as input and returns True 
if all the characters in the string are lowercase letters, 
and False otherwise.
"""
def custom_islower(s):
    has_cased = False
    for c in s:
        if c.isalpha():
            has_cased = True
            if not ('a' <= c <= 'z'):
                return False
    return has_cased

print(custom_islower("hello"))  
