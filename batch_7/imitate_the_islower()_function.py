#imitate islower() function without using islower()

"""
This function takes a string as input and returns True 
if all the characters in the string are lowercase letters, 
and False otherwise.
"""
def imitate_islower(string):
    has_cased = False
    for i in string:
        if i.isalpha():
            has_cased = True
            if not ('a' <= i <= 'z'):
                return False
    return has_cased

print(imitate_islower("hello"))  
