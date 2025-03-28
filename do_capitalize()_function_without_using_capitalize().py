#capitalize first letter without using capitalize()

#ask user for input
string = input("Enter a string: ")


#capitalizes the first letter of the string
def capitalize(string):
    #check if the first letter is lowercase
    if string[0].islower():
        #if it is, convert it to uppercase
        string = string[0].upper() + string[1:]
    return string

#call the function and print the result
print(capitalize(string))