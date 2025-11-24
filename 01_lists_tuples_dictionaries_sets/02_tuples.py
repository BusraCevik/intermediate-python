# ---------------------------------------------------------
# TUPLES IN PYTHON
# Ordered, immutable, allow duplicate elements
# ---------------------------------------------------------

# Creating tuples
mytuple = ("Max", 28, "Boston")
print(mytuple)

# Parentheses are optional for tuples
mytuple = "Max", 28, "Boston"
print(mytuple)

# Single value tuple needs a trailing comma
mytuple = ("Max")
print(type(mytuple))  # str

mytuple = ("Max",)
print(type(mytuple))  # tuple

# Creating a tuple from a list
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------

item = mytuple[2]   # Access using index
print(item)

item = mytuple[-1]  # Access last element
print(item)

# Tuples are immutable – modifying throws an error
# mytuple[0] = "Tim"  # TypeError

# ---------------------------------------------------------
# ITERATION & MEMBERSHIP
# ---------------------------------------------------------

for x in mytuple:
    print(x)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

# ---------------------------------------------------------
# BUILT-IN METHODS
# ---------------------------------------------------------

my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')

print(len(my_tuple))        # Length of tuple
print(my_tuple.count('a'))  # Count occurrences
print(my_tuple.count('b'))
print(my_tuple.index('c'))  # Index of first occurrence

# ---------------------------------------------------------
# CONVERTING LISTS <--> TUPLES
# ---------------------------------------------------------

my_list = list(my_tuple)   # Tuple → List
print(my_list)

my_tuple2 = tuple(my_list)  # List → Tuple
print(my_tuple2)

# ---------------------------------------------------------
# SLICING TUPLES
# ---------------------------------------------------------

a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5]       # Index 2 to 4
print(b)

b = a[:5]        # Start to index 4
print(b)

b = a[2:]        # Index 2 to end
print(b)

b = a[2:5:2]     # Start, end, step
print(b)

b = a[::-1]      # Reverse tuple
print(b)

# ---------------------------------------------------------
# UNPACKING TUPLES
# ---------------------------------------------------------

my_tuple = ("Max", 28, "Boston")
name, age, city = my_tuple

print(name)
print(age)
print(city)

# Unpacking with extended assignment
my_tuple = (0,1,2,3,4)
l1, *i2, i3 = my_tuple
print(l1)  # first element
print(i2)  # middle sequence
print(i3)  # last element

# ---------------------------------------------------------
# PERFORMANCE NOTES
# Tuples are more memory-efficient and faster than lists
# ---------------------------------------------------------

import sys
my_list = [0, 1, 2, "Hello", True]
my_tuple = (0, 1, 2, "Hello", True)

print(sys.getsizeof(my_list), "bytes")   # Memory usage of list
print(sys.getsizeof(my_tuple), "bytes")  # Memory usage of tuple

# Tuples are faster to create as well
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
