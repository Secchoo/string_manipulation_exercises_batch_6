#to lowercase a string without using lower() function

"""
This function converts a string to lowercase
without using the built-in lower() method.
"""

def custom_lower(string):
    result = ""
    for char in string:
        if 'A' <= char <= 'Z':
            # Convert uppercase to lowercase by adjusting ASCII value
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

#print the result
print(custom_lower("HELLO WORLD"))