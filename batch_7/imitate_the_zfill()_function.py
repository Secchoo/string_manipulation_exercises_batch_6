# Imitate zfill() function without using zfill()

"""
This function pads the string on the left with zeros to fill a width.
"""

def imitate_zfill(string, width):
    if len(string) >= width:
        return string  # Return the string as is if its length is greater than or equal to the width
    sign = ''  # Initialize an empty string to store the sign if present
    if string.startswith(('+', '-')):  
        sign, string = string[0], string[1:]  # Extract the sign and the rest of the string
    # Pad the string with zeros on the left, accounting for the sign if present
    return sign + '0' * (width - len(string) - len(sign)) + string



print(imitate_zfill("42", 5))  

