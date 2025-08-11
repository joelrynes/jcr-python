# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {'name':'siva','age':37}

# dictionaries are accessed via keys
print(mydict['name'])

# you can also set dictionary data by creating a new key
mydict["gender"]="male"
print(mydict)
# Trying to access a nonexistent key will produce an error


# To avoid this, you can use the "in" operator to see if a key exists
print("name" in mydict)

# You can retrieve all of the keys and values from a dictionary
print(mydict.keys() )
print(mydict.values())
# You can also iterate over all the items in a dictionary
for k,l in mydict.items():
  print( k,l)