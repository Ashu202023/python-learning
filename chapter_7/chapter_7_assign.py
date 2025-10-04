#7.1
car=input("what kind of rental car they are looking for?")
print(f"\n Let me see if I can find you a {car.title()}.")

#7.2 
number_of_people=int(input(" how many people are in your dinner group?"))
if number_of_people>8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready.")

#7.3 
number=int(input("enter a number,and I will tell you if it is a multiple of 10:"))
if number%10==0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")