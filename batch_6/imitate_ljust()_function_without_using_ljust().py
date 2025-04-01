#to justify a string to the left without using ljust() method

"""
This function justifies a string to the left within a given width without
using the built-in ljust() method.
"""

def custom_ljust(string, width):
    # Check if the width is less than or equal to 0
    if len(string) >= width:
        return string
    return string + ' ' * (width - len(string))

# Test cases
test_str = "hello"
width = 10

result = custom_ljust(test_str, width)
print(f"Result: '{result}'")  
print(f"Length: {len(result)}")
