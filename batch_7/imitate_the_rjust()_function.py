# Imitate rjust() function without using rjust()

"""
This function takes a string and a width as input and
returns the string right-justified in a field of the given width.
"""

def imitate_rjust(string, width, fillchar=' '):
    if len(string) >= width:
        # If the string length is greater than or equal to the width, return it as is
        return string
    else:
        # Add the required number of fill characters to the left of the string
        return fillchar * (width - len(string)) + string



print(imitate_rjust("Hello", 10))  