#do center function without using center

#ask user for input
string = input("Enter a string: ")

#center the string without using center()
#calculate the number of spaces to add on each side
spaces = (80 - len(string)) // 2
#add spaces to the left and right of the string
string = ' ' * spaces + string + ' ' * spaces
#check if the string is odd length and add one space to the right side
if (80 - len(string)) % 2 != 0:
    string += ' '
#check if the string is even length and add one space to the left side
if (80 - len(string)) % 2 == 0:
    string = ' ' + string
#check if the string is odd length and add one space to the left side
if (80 - len(string)) % 2 != 0:
    string = ' ' + string
#check if the string is even length and add one space to the right side
if (80 - len(string)) % 2 == 0:
    string += ' '




#call the function and print the result
print(string)