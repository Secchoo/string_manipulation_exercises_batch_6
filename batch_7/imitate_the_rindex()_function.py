# Imitate rindex() function without using rindex()

"""
This function takes a string and a substring as input and
returns the index of the last occurrence of the substring in the string.
If the substring is not found, it raises a ValueError.
"""

def imitate_rindex(string, sub):
    sub_len = len(sub)  # Get the length of the substring
    for i in reversed(range(len(string) - sub_len + 1)):  # Iterate in reverse
        if string[i:i + sub_len] == sub:  # Check if the substring matches
            return i  # Return the index of the last occurrence
    raise ValueError("Substring not found")  # Raise an error if not found



print(imitate_rindex("Green apples", "apples"))  