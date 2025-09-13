#5-1 
bike = "Ducati"
print("Is bike == 'Ducati'? I predict True.")
print(bike == 'Ducati')  # True

print("\nIs bike == 'Honda'? I predict False.")
print(bike == "Honda")  # False 

car = "Audi"
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

print("\nIs car == 'Audi'? I predict True.")
print(car == 'Audi')  # True

age = 25
print("\nIs age < 30? I predict True.")
print(age < 30)  # True

print("\nIs age > 30? I predict False.")
print(age > 30)  # False

print("\nIs age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)  # True

print("\nIs age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)  # False

print("\nIs age in range(20,30)? I predict True.")
print(age in range(20, 30))  # True

print("\nIs age in range(30,40)? I predict False.")
print(age in range(30, 40))  # False

print("\nIs age in range(20,22)? I predict False.")
print(age in range(20, 22))  # False

#5-2 


# --- String equality / inequality ---
name = "ashu"
print("Is name == 'ashu'? I predict True.")
print(name == 'ashu')  # True

print("\nIs name != 'ashu'? I predict False.")
print(name != 'ashu')  # False

# --- Using lower() ---
print("\nIs 'Ashu'.lower() == 'ashu'? I predict True.")
print("Ashu".lower() == 'ashu')  # True

print("\nIs 'ASHU'.lower() == 'ASHU'? I predict False.")
print("ASHU".lower() == 'ASHU')  # False


# --- Numerical tests ---
number = 23
print("\nIs number > 20? I predict True.")
print(number > 20)  # True

print("\nIs number < 20? I predict False.")
print(number < 20)  # False

print("\nIs number != 20? I predict True.")
print(number != 20)  # True

print("\nIs number >= 20 and number <= 43? I predict True.")
print(number >= 20 and number <= 43)  # True

print("\nIs number >= 20 or number <= 20? I predict True.")
print(number >= 20 or number <= 20)  # True


# --- List membership ---
car_collections = ['bmw', 'audi', 'toyota', 'subaru']
print("\nIs 'bmw' in car_collections? I predict True.")
print('bmw' in car_collections)  # True

print("\nIs 'mercedes' not in car_collections? I predict True.")
print('mercedes' not in car_collections)  # True

print("\nIs 'audi' not in car_collections? I predict False.")
print('audi' not in car_collections)  # False

#5.3
alien_color="green"
if alien_color=="green":
    print("You just earned 5 points")

alien_color="red"
if alien_color=="green":
    print("you just earned 5 points")

     
#5.4
alien_color="red"
if alien_color=="green":
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

#5.5
alien_color="yellow" 
if alien_color=="green":
    print("You just earned 5 points")
elif alien_color=="yellow":
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

alien_color="green" 
if alien_color=="green":
    print("You just earned 5 points")
elif alien_color=="yellow":
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

alien_color="red" 
if alien_color=="green":
    print("You just earned 5 points")
elif alien_color=="yellow":
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

# another way to solve 5.5
alien_colors=["green","yellow","red"]
for alien_color in alien_colors:
    if alien_color=="green":
        print("You just earned 5 points")
    elif alien_color=="yellow":
        print("You just earned 10 points")
    else:
        print("You just earned 15 points")

#5.6
age=5
if age<2:
    print("The person is a baby")
elif age<4:
    print("The person is a toddler.")
elif age<13:
    print("The person is a kid.")
elif age<20:
    print("The person is a teenager.")
elif age<65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#5.7
Favorite_fruits=["mango","banana","grapes"]
if "mango" in Favorite_fruits:
    print("You really like mango!")
if "banana" in Favorite_fruits:
    print("You really like banana!")
if "grapes" in Favorite_fruits:
    print("You really like grapes!")
if "apple" in Favorite_fruits:
    print("You really like apple!")
if "orange" in Favorite_fruits:
    print("You really like orange!")    
    
#5.8 
username=["admin","ashu","john","doe","jane"]
for i in username:
    if i=="admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {i},thank you for logging in again.")
#5.9
username.clear()
if not username:
    print("We need to find some users!")

#5.10
current_users = ["ashu","john","doe","jane","admin"]
new_users = ["Ashu","mike","jane","sara","tom"]

# Create a lowercase list once
current_users_lower = [u.lower() for u in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} is already taken. Please enter a new username.")
    else:
        print(f"{user} is available.")
#5.11 
numbers=list(range(1,10))
for i in numbers:
    if i==1:
        print(f"{i}st")
    elif i==2:
        print(f"{i}nd")
    elif i==3:
        print(f"{i}rd")
    else:
        print(f"{i}th")