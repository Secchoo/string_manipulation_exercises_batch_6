#to justify a string to the left without using ljust() method

"""
This function justifies a string to the left within a given width without
using the built-in ljust() method.
"""

def custom_ljust(s, width):
    if len(s) >= width:
        return s
    return s + ' ' * (width - len(s))

# Test cases
test_str = "hello"
width = 10

result = custom_ljust(test_str, width)
print(f"Result: '{result}'")  
print(f"Length: {len(result)}")
