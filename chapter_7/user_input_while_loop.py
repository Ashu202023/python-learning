# How the input() function works
message=input("tell me something and I will repeat it back to you: ")
print(message)

#writing clear prompts

name=input("please enter your name:")
print(f"\nHello,{name}!")

prompt="If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your first name? "
name=input(prompt)
print(f"\nHello,{name}!")

#using int() to accept numerical input
age=input("how old are you?")
print(age)
print(type(age)) # by default input() function takes input as string
age=int(age) # convert string to integer using int() function
print(age)
print(type(age))
print(age>18)

height=input("enter your height in inches:")
height=int(height)
if height>=49:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")

# the modulo operator

number=input("enter a number, and I will tell you if it is even or odd:")
number=int(number)
if number%2 ==0:
    print(f"\n {number} is an even number.")
else:
    print(f"\n {number} is an odd number.")

###########################################


