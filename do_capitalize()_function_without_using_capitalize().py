#capitalize first letter without using capitalize()

#ask user for input
string = input("Enter a string: ")


#capitalizes the first letter of the string
if string[0].islower():
    string = string[0].upper() + string[1:]
else:
    string = string[0] + string[1:]
    

#call the function and print the result
print(string)