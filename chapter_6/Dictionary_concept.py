# A simple Dictionary: collection of key-value pairs.its written in curly braces{}
# Each key is separated from its value by a colon(:),the key-value pairs are separated by commas(,)
# and the whole thing is enclosed in curly braces({}).
alien_0={"color":"green","points":5}

#accessing values in a dictionary
print(alien_0["color"])
print(alien_0["points"])

new_points=alien_0["points"]
print(f"You just earned {new_points} points!")

#Adding new key-value pairs,Dictioniary retain the order in which we add the key-value pairs
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#starting with an empty dictionary
alien_1={}
alien_1["color"]="red"
alien_1["points"]=10
print(alien_1)

#modifiing values in a dictionary
print(f"the alien is {alien_1["color"]}.")
alien_1["color"]="Orange"
print(f"the aliem color is now {alien_1['color']}.")

alien_2={"x_position":0,"y_position":25,"speed":"fast"}
print(f"Original position:({alien_2['x_position']},{alien_2["y_position"]}).")
#move the alien to the right
if alien_2["speed"]=="slow":
    x_increment=1
elif alien_2["speed"]=="medium":
    x_increment=2
else:
    x_increment=3
alien_2["x_position"]=alien_2["x_position"] + x_increment 
print(f"New Position:({alien_2["x_position"]},{alien_2["y_position"]}).")

#Removing key-value pairs
alien_3={"color":"green","points":5}
print(alien_3)
del alien_3["points"] #Be aware that the deleted key-value pair is removed permanently

print(alien_3)
del alien_3

# print(alien_3) #this will give error as alien_3 is deleted

# A Dictionary of similar objects
Favorite_languages={
    "ashutosh":"python",
    "aswani":"c",
    "nikhil":"java",
    "rahul":"javascript",
    "kanishka":"ruby",
    }
language=Favorite_languages["ashutosh"].title()
print(f"Ashutosh's favourite language is {language}.")

# using get() to Access values: key in square bracket[] doesn't exist in dictionary give error
alien_5={"color":"red","speed":"slow"}

# print(alien_5["points"]) # give keyerror,to avoid this we can use get() method
#get() method returns None if the key doesn't exist instead of giving an error,take key as first argument
#and second optional argument as value to return if the key doesn't exist

point_value=alien_5.get("points","No points value assigned.")
print(point_value)
print(alien_5.get("age"))# give "None" as output,None is a special value in python 
#that represents the absence of a value.

# looping through a Dictionary:
#looping through all key-values pairs 
user_0={
    "username":"ashutosh_k",
    "first_name":"ashutosh",
    "last_name":"Kumar",
 }

for key,value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")
#items() method returns a list of key-value pairs in a dictionary
for name,language in Favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

#looping through all the keys in a dictionary

for name in Favorite_languages.keys(): #keys() method returns a list of all the keys in the dictionary,its optional. 
    print(name.title())

for name in Favorite_languages: #this also works the same as above
    print(name.title())

friends=["aswani","nikhil"]

for name in Favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language=Favorite_languages[name].title()
        print(f"\t {name.title()}, I see your favourite lanaguage is {language}!")

if "ayaan" not in Favorite_languages.keys():
    print("Ayaan, please take our poll!")

#looping through a dictionary's keys in a particular order

for name in sorted(Favorite_languages.keys()): #sorted() function returns a sorted list of keys
    print(f"{name.title()}, thank you for taking the poll.")

#looping through all values in a dictionary



