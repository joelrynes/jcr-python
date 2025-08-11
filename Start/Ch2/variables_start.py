# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint)
print(myfloat)
print(mystr)
print(mybool)
# Operators are used to perform operations on variables
print(myint+myint)
print(myint-myint)
print(myint*myint)
print(myint/myint)
print(myint%myint)

# Logical and comparison operators 
print(myint<myfloat)
print(myint>myfloat)
print(myint<=myfloat)
print(myint==myfloat)

# re-declaring a variable works
myint=15
print(myint)