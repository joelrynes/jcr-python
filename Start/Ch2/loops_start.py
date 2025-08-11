# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop


# define a for loop

for si in range(0,10):
  total=0
  total+si
print(total+si)


numb=[1,2,3,4,5,6,7]
for n in numb:
  print(n)
# use a for loop over a collection


# use the break and continue statements
for n in numb:
  if n==5:
    continue
  print(n)

# using the enumerate() function to get an index and an item
for i,n in enumerate(numb):
  print(i,n)
