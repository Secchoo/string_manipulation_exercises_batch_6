#imitate rindex() function without using rindex()

"""
This function takes a list and an element as input and
returns the index of the last occurrence of the element in the list.
"""

def imitate_rindex(string, sub):
    sub_len = len(sub)
    for i in reversed(range(len(string) - sub_len + 1)):
        if string[i:i+sub_len] == sub:
            return i
    raise ValueError("Substring not found")

print(imitate_rindex("Green apples", "apples"))