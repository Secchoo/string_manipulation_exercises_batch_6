#imitate rjust() function without using rjust()

"""
This function takes a string and a width as input and
returns the string right-justified in a field of the given width."
"""

def imitate_rjust(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    else:
        return fillchar * (width - len(string)) + string
    
print(imitate_rjust("Hello", 10))  