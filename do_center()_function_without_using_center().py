#do center function without using center

#ask user for input
string = input("Enter a string: ")

#center the string
total_padding = max(0, width - len(string))
left_padding = total_padding // 2
right_padding = total_padding - left_padding
return string * left_padding + string + string * right_padding

#call the function and print the result
print(string)