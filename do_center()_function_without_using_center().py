#do center function without using center

#ask user for input
string = input("Enter a string: ")

#center the string
if len(string) % 2 == 0:
    string = " " + string + " "
else:
    string = " " + string + "  "

#call the function and print the result
print(string)