#imitate_the index() function without using index()

"""
This function takes a list and an element as input and
returns the index of the first occurrence of the element in the list.
"""

def imitate_index(string, sub):
    sub_len = len(sub)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub:
            return i
    raise ValueError("substring not found")

print(imitate_index("abab", "ba"))