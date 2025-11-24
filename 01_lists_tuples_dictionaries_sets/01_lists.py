# ---------------------------------------------------------
# LISTS IN PYTHON
# Ordered, mutable, allow duplicate elements
# ---------------------------------------------------------

# Creating simple lists
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]  # Lists can hold mixed data types
print(mylist2)

# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------

item = mylist[0]   # First element
print(item)

item = mylist[-1]  # Last element using negative index
print(item)

# Iterate through the list
for i in mylist:
    print(i)

# Check if an element exists in the list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# ---------------------------------------------------------
# LIST METHODS
# ---------------------------------------------------------

mylist.append("lemon")  # Adds item to the end
print(mylist)

mylist.insert(1, "blueberry")  # Inserts at index 1
print(mylist)

item = mylist.pop()  # Removes and returns the last item
print(mylist)

mylist.remove("apple")  # Removes the first occurrence of "apple"
print(mylist)

# Other useful list methods (uncomment to use):
# mylist.clear()        # Removes all elements
# mylist.reverse()      # Reverses the list in place
# mylist.sort()         # Sorts the list in place (ascending)
# newlist = sorted(mylist)  # Returns a new sorted list without modifying original

# Replicating lists
# mylist = [0] * 5   # Creates [0, 0, 0, 0, 0]

# Concatenation
# new_list = mylist + mylist2

# ---------------------------------------------------------
# LIST SLICING
# ---------------------------------------------------------

mylist = [1,2,3,4,5,6,7,8,9]

a = mylist[1:5]    # Slice from index 1 to 4
print(a)  # [2, 3, 4, 5]

a = mylist[::2]    # Step 2 → every second item
print(a)  # [1, 3, 5, 7, 9]

a = mylist[::-1]   # Reverse the list
print(a)

# ---------------------------------------------------------
# COPYING LISTS (IMPORTANT!)
# ---------------------------------------------------------

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org  # This copies the reference, not the values

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

# Both lists change because they refer to the same memory location

# Correct way to copy:
# list_cpy = list_org.copy()
# OR
# list_cpy = list(list_org)
# OR
# list_cpy = list_org[:]

# ---------------------------------------------------------
# LIST COMPREHENSION
# ---------------------------------------------------------

mylist = [1,2,3,4,5,6]

# Create a new list with squared values
b = [i * i for i in mylist]
print(b)
