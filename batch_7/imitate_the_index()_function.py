#imitate_the index() function without using index()

"""
This function takes a list and an element as input and
returns the index of the first occurrence of the element in the list.
"""

def imitate_index(s, sub):
    sub_len = len(sub)
    if sub_len == 0:
        return 0
    for i in range(len(s) - sub_len + 1):
        if s[i:i+sub_len] == sub:
            return i
    raise ValueError("Substring not found")

print(imitate_index("Green apples", "Green"))