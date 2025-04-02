#imitate the count() function without using count()

"""
This function takes a list and an element as input and 
returns the number of occurrences of the element in the list.
It uses a for loop to iterate through the list and a counter 
variable to keep track of the number of occurrences.
"""

def imitate_count(string, sub):
    count = 0  # Initialize a counter to track occurrences
    sub_len = len(sub)
    
    if sub_len == 0:
        # If the substring is empty, it matches between every character
        return len(string) + 1
    
    # Iterate through the string to find all occurrences of the substring
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub:
            count += 1  # Increment the counter if a match is found
    
    return count  # Return the total count of occurrences

print(imitate_count("Hello world, Hello Everyone", "Hello"))