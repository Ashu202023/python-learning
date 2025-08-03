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

for car in cars 
    print(car.title(), "is a great car.")  # this will raise a syntax error because of the missing colon at the end of the for loop.
    