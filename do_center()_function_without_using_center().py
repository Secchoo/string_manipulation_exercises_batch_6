#do center function without using center

# Get input from the user
string = input("Enter the string: ")
width = int(input("Enter the width: "))

# Calculate padding
if len(string) >= width:
    centered = string
else:
    total_pad = width - len(string)
    left_pad = total_pad // 2
    right_pad = total_pad - left_pad
    centered = ' ' * left_pad + string + ' ' * right_pad

# Output the result
print(centered)