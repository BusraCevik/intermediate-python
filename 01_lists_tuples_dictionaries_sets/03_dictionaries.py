# ---------------------------------------------------------
# DICTIONARIES IN PYTHON
# Key-Value pairs, unordered (3.7+ ordered), mutable
# ---------------------------------------------------------

# Creating dictionaries
mydict1 = {"name": "Max", "age": 25, "city": "London"}  # Using curly braces
print(mydict1)

mydict2 = dict(name="Marry", age=20, city="Boston")     # Using dict() constructor
print(mydict2)

# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------

value = mydict1["name"]  # Access value by key
print(value)

# Adding or updating a key-value pair
mydict1["email"] = "max@xyz.com"        # Add new key
print(mydict1)

mydict1["email"] = "maxmax@xyz.com"     # Update existing key
print(mydict1)

# ---------------------------------------------------------
# REMOVING ELEMENTS
# ---------------------------------------------------------

removed_value = mydict1.pop("age")  # Removes 'age' key and returns its value
print(removed_value)
print(mydict1)

removed_item = mydict1.popitem()     # Removes last inserted key-value pair
print(removed_item)
print(mydict1)

# ---------------------------------------------------------
# CHECKING KEYS
# ---------------------------------------------------------

if "name" in mydict1:
    print(mydict1["name"])

# Accessing a key safely
try:
    print(mydict1["age"])  # KeyError if 'age' doesn't exist
except KeyError:
    print("Error: key does not exist")

# ---------------------------------------------------------
# ITERATION
# ---------------------------------------------------------

# Iterate over keys
for key in mydict1:
    print(key)

for key in mydict1.keys():
    print(key)

# Iterate over values
for value in mydict1.values():
    print(value)

# Iterate over key-value pairs
for key, value in mydict1.items():
    print(key, value)

# ---------------------------------------------------------
# COPYING DICTIONARIES
# ---------------------------------------------------------

# Assignment copies the reference, not the data
mydict_cpy = mydict1
print(mydict_cpy)
print(mydict1)

# To create a true copy, use .copy() or dict()
mydict_copy_safe = mydict1.copy()

# ---------------------------------------------------------
# UPDATING DICTIONARIES
# ---------------------------------------------------------

mydict3 = {"name": "Busra", "age": 24, "city": "Krakow", "email":"busra@.com"}
mydict4 = dict(name="Fred", age=27, city="Paris")

mydict3.update(mydict4)  # Updates values of mydict3 with keys from mydict4
print(mydict3)
print(mydict4)  # mydict4 remains unchanged

# ---------------------------------------------------------
# DICTIONARIES WITH NON-STRING KEYS
# ---------------------------------------------------------

mydict5 = {3:9, 6:36, 9:81}
print(mydict5)

value = mydict5[3]  # Access value by key
print(value)

mytuple3 = (8, 7)
mydict = {mytuple3 : 15}  # Tuples can be keys if they are immutable
print(mydict)
