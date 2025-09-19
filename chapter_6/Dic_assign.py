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

