# ---------------------------------------------------------
# COLLECTIONS MODULE IN PYTHON
# Provides specialized container datatypes:
# Counter, namedtuple, OrderedDict, defaultdict, deque
# ---------------------------------------------------------

# ---------------------------------------------------------
# COUNTER
# Counts hashable objects and returns a dictionary-like object
# ---------------------------------------------------------

from collections import Counter

a = "aaaaaaaabbbbbccc"
my_counter = Counter(a)

print(my_counter)               # Counts occurrences of each character
print(my_counter.most_common(3)) # Top 3 most common elements
print(my_counter.items())        # Items as (element, count)
print(my_counter.keys())         # Unique elements
print(my_counter.values())       # Counts only
print(list(my_counter.elements()))  # Iterator over elements repeating by count


# ---------------------------------------------------------
# NAMEDTUPLE
# Tuple with named fields → lightweight object-like structure
# ---------------------------------------------------------

from collections import namedtuple

Point = namedtuple("Point", "x y")
pt = Point(1, -4)

print(pt.x, pt.y)   # Access by attribute name (not only by index)


# ---------------------------------------------------------
# ORDEREDDICT
# Preserves insertion order (normal dicts do this by default in Python 3.7+)
# ---------------------------------------------------------

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)


# ---------------------------------------------------------
# DEFAULTDICT
# Automatically creates a default value for missing keys
# ---------------------------------------------------------

from collections import defaultdict

d = defaultdict(int)   # Default value = 0 (for int)
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d['g'])   # Key doesn't exist → returns default 0 instead of error


# ---------------------------------------------------------
# DEQUE (DOUBLE-ENDED QUEUE)
# Fast appends/pops from both ends (better than list performance)
# ---------------------------------------------------------

from collections import deque

dq = deque()

dq.append(1)         # Add to the right
dq.appendleft(5)     # Add to the left
print(dq)

dq.pop()             # Remove from right
print(dq)

dq.popleft()         # Remove from left
print(dq)

dq.extend([4, 5, 6])     # Extend to the right
print(dq)

dq.extendleft([7, 8, 9]) # Extend to the left (reversed order)
print(dq)

dq.rotate(2)         # Rotate right by 2 → elements move to the right end
print(dq)
