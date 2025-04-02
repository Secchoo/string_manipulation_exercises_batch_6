#imitate removesuffix() function without using removesuffix()

"""
This function takes a string and a suffix as input and 
returns the string with the suffix removed if it is present, 
otherwise returns the original string.
"""

def imitate_removesuffix(s, suffix):
    if suffix and len(s) >= len(suffix) and s[-len(suffix):] == suffix:
        return s[:-len(suffix)]
    return s

print(imitate_removesuffix("HelloWorld", "World"))