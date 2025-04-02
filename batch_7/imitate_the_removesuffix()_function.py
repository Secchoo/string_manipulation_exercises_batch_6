#imitate removesuffix() function without using removesuffix()

"""
This function takes a string and a suffix as input and 
returns the string with the suffix removed if it is present, 
otherwise returns the original string.
"""

def imitate_removesuffix(string, suffix):
    if suffix and len(string) >= len(suffix) and string[-len(suffix):] == suffix:
        return string[:-len(suffix)]
    return string

print(imitate_removesuffix("HelloWorld", "World"))