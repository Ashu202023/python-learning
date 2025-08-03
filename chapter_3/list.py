pets=["dog","Cat","rabbit","fish","Parrot"]
print(pets)        
print(pets[0].upper())
print(pets[-2].title())
message=f"My favourite pet is {pets[0].title()}."
print(message)

# modifying,adding and removing elements 
# modifying an element:
pets[2]="hamster"
print(pets)
pets[-1]="macaw"
print(pets)

# adding an element into a list 
# append()-add element at the end of the list 
pets.append("turtle")
print(len(pets))
print(pets)

transport_vehicle=[]
n=int(input("enter the number of transport vehicles: "))
for i in range(n):
    transport_vehicle.append(input("enter a transport vehicle: "))
print(transport_vehicle)

# insert element into a list : insert() method 
transport_vehicle.insert(0,"BMW bike")
print(transport_vehicle)
transport_vehicle.append("yamaha R15")
print(transport_vehicle)
transport_vehicle.insert(2,"mercedes benz")
print(transport_vehicle)

#removing elements from a list,either by value or by index 
#  del: removes element by index 
del transport_vehicle[0]
print(transport_vehicle)

#pop(): removes element by index and returns it

removed_vehicle=transport_vehicle.pop()
print(f"the last vehicle i owned was {removed_vehicle.title()}.")

print(transport_vehicle) 

first_owned_vehicle=transport_vehicle.pop(0)
print(f"my first owned vehicle was {first_owned_vehicle.title()}.")
print(transport_vehicle)

# removng an element by value : remove() method 
# it removes the first occurrence of the value,more than one occurrence will not be removed 


pets.remove("Cat")
print(pets)

too_expensive="macaw"
pets.remove(too_expensive)
print(f" {too_expensive.title()} is too expensive for me.")
print(pets)

# oraganizing a list : sort() and sorted() methods

# sort() method sorts the list in place,modifying the original list.permanent change the list.
pets.sort()
print("after sorted",pets)

pets.sort(reverse=True) # sorts the list in reverse order permanently
print(f"after sorted in reverse order:{pets}.")

#sorted() method sorts the list temporarily,does not modify the original list. 
vehicle=["car","bike","helicopter","train","bus","truck"]
print(sorted(vehicle))#sorted in ascending order temporarily
print(sorted(vehicle,reverse=True))#sorted in descending order temporarily
print(vehicle)

# printing the list in reverse order:reverse() method 
# reverse() method reverses the order of the list permanently

vehicle.reverse()
print(vehicle)

#finding the length of a list : len() function
print(len(vehicle)) 

