# tuples:cannot be changed,immutable.
# tuples are defined using parentheses()
dimensions=(200,50)
print(dimensions[0])  # accessing the first element
print(dimensions[1])  # accessing the second element
# dimensions[0]=250  # this will raise an error because tuples are immutable
my_tuple=(3) # this will not create a tuple, it will create an integer
print(type(my_tuple))  # this will print 3, not a tuple 
my_tuple1=(3,) # this will create a tuple with one element
print(type(my_tuple1))  # this will print <class 'tuple'>, a tuple

# looping through a tuple 
for dimension in dimensions:
    print(dimension)

# writing over a tuple 
# we can't change a tuple, but we can assign a new tuple with the same name. 
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
