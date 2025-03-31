#to imitate swapcase() function without using swapcase() function

"""
This function swaps the case of each character in a 
string without using the built-in swapcase() method.
"""

def custom_swapcase(string):
    swapped = []
    for i in string:
        if 'A' <= i <= 'Z':
            swapped.append(chr(ord(i) + 32))
        elif 'a' <= i <= 'z':
            swapped.append(chr(ord(i) - 32))
        else:
            swapped.append(i)
    return ''.join(swapped)


#print the result
print(custom_swapcase("Hello World"))