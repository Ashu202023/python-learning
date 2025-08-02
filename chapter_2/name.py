# name="ashutosh kumar"
# print(name.title())
# print(name.upper())
# print(name.lower())
first_name="aswani"
last_name="kumar"
full_name=f"{first_name} {last_name}"
print(full_name)
# print(f"Hello,{full_name.title()}!")
# message=f"Hello, {full_name.title()}!"
# print(message)
print("\tPython")
print("python")
# print("Languages:\nPython\nC\nJava")
print("languages:\n\tPython\n\tC\n\tJava")
fav_language="Python "
print(fav_language.rstrip()) #temporary remove right side whitespace
fav_language=fav_language.rstrip() #permanent remove white space by assigning

fav_lang=" python "
print(fav_lang.rstrip())
print(fav_lang.lstrip())
print(fav_lang.strip())

# Removing Prefixes
address_url="http://nostarch.com"
simple_url=address_url.removeprefix("http://")
print(simple_url)
print(address_url)