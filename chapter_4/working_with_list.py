#looping through an entire list: same actions for each element in the list.
magicians=["harry houdini","david blaine","dynamo"]
for magician in magicians:
    print(f"{magician.title()} is a great magician.")
    print(f"I can't wait to see {magician.title()} perform.\n")
print("thank you,everyone for the wonderful magic show!")

#avoiding indentation errors
# if you forget to indent the code inside the loop,python will raise an indentation error.
cars=["bmw","audi","toyota","subaru"]
for car in cars:
#print(car) // this will raise an indentation error
    print(car.title(), "is a great car.")

message="I love programming in python."
    #print(message) // this will raise an indentation error
print(message)

# for car in cars
    # print(car.title(), "is a great car.")  # this will raise a syntax error because of the missing colon at the end of the for loop.

#making numerical lists 

#using the range() function to generate a list of numbers
for value in range(1,5): #// range(start,stop) generates numbers from start to stop-1
    print(value)

for x in  range(6): # // range(stop) generates numbers from 0 to stop-1
    print(x)

#using the range() function to create a list of numbers 

numbers=list(range(1,6)) # creates a list of numbers from 1 to 5
print(numbers)

even_numbers=list(range(2,11,2))# creates a list of even numbers from 2 to 10
print(even_numbers)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#simple statistics with a list of numbers 
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))  # minimum value in the list
print(max(digits))  # maximum value in the list 
print(sum(digits))  # sum of all values in the list

#List comprehensions: a concise way to create lists 
