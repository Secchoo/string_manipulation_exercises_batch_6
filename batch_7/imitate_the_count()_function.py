#imitate the count() function without using count()

"""
This function takes a list and an element as input and 
returns the number of occurrences of the element in the list.
It uses a for loop to iterate through the list and a counter 
variable to keep track of the number of occurrences.
"""

def imitate_count(string, sub):
    count = 0
    sub_len = len(sub)
    if sub_len == 0:
        return len(string) + 1
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub:
            count += 1
    return count

print(imitate_count("abab", "aba"))