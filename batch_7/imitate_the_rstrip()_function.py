#imitate rstrip() function without using rstrip()

""""
This function takes a string as input and returns the string 
with trailing whitespace removed.
"""

def imitate_rstrip(string):
    end = len(string)
    while end > 0 and string[end - 1] == ' ':
        end -= 1
    return string[:end]

print(imitate_rstrip("Hello World    "))