# Imitate removesuffix() function without using removesuffix()

"""
This function takes a string and a suffix as input and 
returns the string with the suffix removed if it is present, 
otherwise returns the original string.
"""

def imitate_removesuffix(string, suffix):
    # Check if the suffix is non-empty and matches the end of the string
    if suffix and len(string) >= len(suffix) and string[-len(suffix):] == suffix:
        # Remove the suffix by slicing the string
        return string[:-len(suffix)]
    # Return the original string if the suffix is not present
    return string



print(imitate_removesuffix("HelloWorld", "World"))