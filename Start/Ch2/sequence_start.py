# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
li = [1, 2, "one", "two", True]
tu = (1,2,2,"one","two")
print(li)
print(tu)

# to access a member of a sequence type, use []
print(li[1])
print(tu[1])
# add a list to another list
print(li+li)

# use slices to get parts of a sequence
print(li[0:4])
print(li[:5])
# you can use slices to reverse a sequence
print(li[::-1])

# Tuples are like lists, but they are immutable
#tu[0]=3
#print(tu)

# Sets are also sequences, but they contain unique values
se= {0,0,1,1,2}
print(se)
# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
