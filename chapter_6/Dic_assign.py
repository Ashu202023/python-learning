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


