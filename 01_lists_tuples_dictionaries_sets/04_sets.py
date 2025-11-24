# ---------------------------------------------------------
# SETS IN PYTHON
# Unordered, mutable, no duplicates
# ---------------------------------------------------------

# Creating sets
myset = {1, 2, 3, 1, 2}  # Duplicates are automatically removed
print(myset)

myset2 = set("Hello")     # Create a set from iterable (string)
print(myset2)

# Empty set
myset3 = {}               # This creates a dictionary, not a set
print(type(myset3))       # <class 'dict'>

myset3 = set()            # Correct way to create an empty set
print(type(myset3))       # <class 'set'>

# Adding elements
myset.add(1)
myset.add(2)
myset.add(3)

# Removing elements
myset.remove(1)           # Raises KeyError if element not found
myset.discard(4)          # Does not raise error if element not found

# myset.clear()            # Removes all elements

# Pop an arbitrary element
myset.pop()

# Iterating over a set
for i in myset:
    print(i)

# Membership test
if 1 in myset:
    print("yes")
else:
    print("no")

# ---------------------------------------------------------
# SET OPERATIONS
# ---------------------------------------------------------

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union: combines elements of both sets without duplicates
u = odds.union(evens)
print(u)

# Intersection: elements common to both sets
i = odds.intersection(evens)
print(i)

# Difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

# Symmetric difference: elements in either set but not in both
diff2 = setA.symmetric_difference(setB)
print(diff2)

# In-place update operations
setA.update(setB)                    # Add elements from setB
print(setA)

setA.intersection_update(setB)       # Keep only common elements
print(setA)

setA.difference_update(setB)         # Remove elements found in setB
print(setA)

setA.symmetric_difference_update(setB)  # Keep elements in either set but not both
print(setA)

# Subset, Superset, Disjoint
print(setA.issubset(setB))       # True if setA is subset of setB
print(setA.issuperset(setB))     # True if setA is superset of setB
print(setA.isdisjoint(setB))     # True if no common elements

# ---------------------------------------------------------
# FROZENSET
# Immutable set
# ---------------------------------------------------------

a = frozenset([1, 2, 3, 4])
# a.add(2)   # Not allowed, frozenset is immutable
print(a)
