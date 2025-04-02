# Imitate the index() function without using index()

"""
This function takes a string and a substring as input and
returns the index of the first occurrence of the substring in the string.
If the substring is not found, it raises a ValueError.
"""

def imitate_index(string, sub):
    # Validate inputs
    if string is None or sub is None:
        raise ValueError("Inputs cannot be None")
    sub_len = len(sub)
    
    # Handle empty substring case
    if sub_len == 0:
        return 0
    
    # Iterate through the string to find the substring
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == sub:
            return i
    
    # Raise an error if the substring is not found
    raise ValueError("Substring not found")


print(imitate_index("Green apples", "Green"))  # Output: 0
print(imitate_index("Green apples", "apples"))  # Output: 6