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
print(age0>=21 and age1<21)  

