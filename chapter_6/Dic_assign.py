#6.1
person_info={
    "first_name":"Ashutosh",
    "last_name":"Kumar",
    "age":25,
    "city":"Bangalore",
    }
print(person_info.get("first_name"))
print(person_info.get("last_name"))
print(person_info.get("age"))
print(person_info["city"])

#6.2
people_fav_numbers={
    "ashutosh":7,
    "aswani":3,
    "ritik":9,
    "nikhil":5,
    "rahul":11,
}
for k,v in people_fav_numbers.items():
    print(f"{k.title()}'s favourite number is {v}.")

#6.3

glossary={
    "list":"A collection of items in a particular order.",
    "tuple":"A collection of items which is ordered and unchangeable.",
    "dictionary":"A collection of key-value pairs.",
    "loop":"A way to iterate over a block of code multiple times.",
    "conditional statement":"A set of rules performed if a certain condition is met.",
}

for word,meaning in glossary.items():
    print(f"{word.title()} : \n {meaning}\n")

#6.4
glossary["set"]="A collection of unique items."
glossary["string"]="A collection of characters."
glossary["float"]="A number with a decimal point."
glossary["integer"]="A whole number."
glossary["boolean"]="A value that is either True or False."

for word,meaning in glossary.items():
    print(f"{word.title()} \n : {meaning}\n")

#6.5
rivers={
    "nile":"Egypt",
    "ganga":"India",
    "amazon":"Brazil",
}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print(f"\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print(f"\nThe following countries are included in the dictionary:")
for country in rivers.values():
    print(country.title())

#6.6
Favorite_languages={
    "ashutosh":"python",
    "aswani":"c",
    "nikhil":"java",
    "rahul":"javascript",
    "kanishka":"ruby",
    }
people=["ashutosh","aswani","nikhil","rahul","kanishka","ritik","mohit"]   
for person in people:
    if person in Favorite_languages:
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"{person.title()},please take the poll.")


#6-7
people={
    "ashutosh":{
        "first_name":"ashutosh",
        "last_name":"kumar",
        "age":25,
        "city":"bangalore",
        },
    "aswani":{
        "first_name":"aswani",  
        "last_name":"kumar",
        "age":24,
        "city":"hyderabad",
        },
    "nikhil":{
        "first_name":"nikhil",  
        "last_name":"sharma",
        "age":26,
        "city":"delhi",
        },
}

for username,info in people.items():
    print(f"username:{username}")
    print(f"full_name:{info['first_name']} {info['last_name']}")
    print(f"age:{info['age']}")
    print(f"city:{info['city']}\n")

#6-8
dog={
    "name":"rocky",
    "breed":"labrador",
    "owner":"ashutosh",
}
cat={
    "name":"kitty",
    "breed":"persian",
    "owner":"aswani",
}

pets=[dog,cat]
for pet in pets:
    print(f"pet-name:{pet['name']}")
    print(f"pet-breed:{pet['breed']}")
    print(f"pet_owner:{pet['owner']}\n")

#6-9

Favourite_places={
    "Rahul":["agra","delhi","mumbai"],
    "ashutosh":["bangalore","manali"],
    "nikhil":["goa","delhi"],
    "aswani":[  "hyderabad","chennai","pune"],
}

for name,places in Favourite_places.items():
    print(f"{name.title()}'s favourite place is :")
    for place in places:
        print(f"\t{place.title()}")

#6-10
favourite_numbers={
    "ashutosh":[7,3],
    "aswani":[3,9],
    "nikhil":[5,11,34],
    "rahul":[11,13,69,61,62],
    "kanishka":[2,4],
}
for name,numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")

#6-11
cities={
    "delhi":{"country":"india",
             "population":20000000,
             "fact":"capital of india",
            },
    "bangalore":{"country":"india",
                 "population":10000000,
                 "fact":"it is silicon valley of india",
                },
    "paris":{"country":"france",
            "population":11000000,     
            "fact":"city of lights",
            },
}

for city,information in cities.items():
    print(f"city:{city.title()}:")
    for k,v in information.items():
        print(f"\t{k}:{v}")
