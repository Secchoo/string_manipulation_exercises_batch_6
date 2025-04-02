# Imitate islower() function without using islower()

"""
This function takes a string as input and returns True 
if all the characters in the string are lowercase letters, 
and False otherwise.
"""

def imitate_islower(string):
    has_cased = False  # Tracks if the string contains any alphabetic characters
    for i in string:
        if i.isalpha():  # Check if the character is alphabetic
            has_cased = True  
            if not ('a' <= i <= 'z'):  # Check if the character is not lowercase
                return False  # Return False if a non-lowercase character is found
    return has_cased 


print(imitate_islower("hello"))
