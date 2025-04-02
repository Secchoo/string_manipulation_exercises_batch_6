#imitate zfill() function without using zfill()

"""
This function pads the string on the left with zeros to fill a width.
"""

def imitate_zfill(string, width):
    if len(string) >= width:
        return string
    sign = ''
    if string.startswith(('+', '-')):
        sign, string = string[0], string[1:]
    return sign + '0' * (width - len(string) - len(sign)) + string


print(imitate_zfill("42", 5))

