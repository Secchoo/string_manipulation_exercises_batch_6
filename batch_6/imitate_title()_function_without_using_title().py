#to imitate title() function without using title() function

"""
This function capitalizes the first letter of each word in a string
"""

def custom_title(string):
    result = []
    next_word_start = True  # Flag to track if the next character starts a new word
    for i in string:
        if next_word_start:
            # Check if the character is cased (uppercase or lowercase)
            if i.isupper() or i.islower():
                result.append(i.upper())
                next_word_start = False
            else:
                # Non-cased character: leave as-is, next character could start a word
                result.append(i)
                next_word_start = True
        else:
            if i.isupper() or i.islower():
                # Within a word: lowercase the character
                result.append(i.lower())
                next_word_start = False
            else:
                # Non-cased character ends the current word
                result.append(i)
                next_word_start = True
    return ''.join(result)

#print the result
print(custom_title("hello world"))