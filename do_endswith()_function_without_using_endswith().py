#use endwith() function without using endswith() function

#ask user for input
string = input("Enter a string: ")

#endwith function without using endswith()
if string[-3:] == "ing":
    string = string + "ed"
else:
    string = string + "ing"

#call the function and print the result
print(string)