cars=["audi","bmw","subaru","toyota"]
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional tests 
#checking for equality 
car="bmw"
print(car=='bmw')  # True   
print(car=='audi')  # False

#ignoring case when checking for equality 
car="Audi"
print(car=='audi') # False
print(car.lower()=='audi') # True,does not change the original string
print(car) # Audi

#checking for inequality (!=) 
requested_topping='mushrooms'
if requested_topping != 'tomatoes':
    print("Hold the tomatoes!")

#Numerical comparisons 
age=19
print(age==19)  # True

answer=17
if answer != 42:
    print("That is not the correct answer. Please try again.")

age=19 
print(age<21)  # True
print(age<=21)  # True
print(age>21)  # False
print(age>=21)  # False

# checking multiple conditions : "and" and "or" 
age0=22
age1=18
print(age0>=21 and age1>=21)  #False, both conditions must be true
print(age0>=21 or age1>=21)  # True, at least one condition is true
print(age0>=21 and age1<21)  # True 
print(age0<21 or age1<21)  # True

#checking whether a value is in a list 
# in operator
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings) # True
print("pepperoni" in requested_toppings) # False

#checking whether a value is not in a list
# not in operator
banned_users=['andrew','carolina','david']
user="ashu"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#boolean expressions : keep track of conditions with boolean values,whether the condition is true or false
game_active=True 
can_edit=False 


# If statements : a block of code that executes only if a certain condition is true
age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if -else statements : provides one alternative path of execution
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else chain : when you have more than two possible paths of execution

age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


price=0
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10

print(f"Your admission cost is ${price}.")

#using mutiple elif blocks 
age=65 
if age<4:
    price=0
elif age<18:
    price=5 
elif age<65:
    price=10
else:
    price=3
print(f"your ticket price is ${price}.")

# omitting the else block : sometimes you may not need an else block at the end of an if-elif chain
age=12
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=2
print(f"Your ticket price is ${price}.")

"""The else block catches anything not matched by 
if or elif, which may include invalid or malicious
 data. Prefer a final elif for specific conditions
and omit else to ensure your code runs only under intended scenarios"""

#testing multiple conditions:if want to check more than one condition at a time
requested_toppings=['mushrooms','extra cheese']
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\n Finished making your pizza!")

#using if-else with lists
requested_toppings=['mushrooms','green peppers','extra cheese'] 

if "mushrooms" in requested_toppings:# only this block will be executed,leave others
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings: #skips this block,though condition is true
    print("Adding extra cheese.")

print("\n Finished making your pizza!")

"""Use if-elif-else when only one
 block should run; use separate if statements 
 when multiple blocks may run."""

#Using if statements with lists
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\n Finished making your pizza!")

# checking that a list is not empty
requested_toppings=[]

if requested_toppings: # evaluates to true if list is not empty
    for requested_topping in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("\n Finished making your pizza!")
else:
    print("Are you sure that you want a plain pizza?")

#using multiple lists
available_toppings=["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings=["mushrooms","french fries","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("\n Finished making your pizza!")

