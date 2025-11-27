# ---------------------------------------------------------
# COLLECTIONS IN PYTHON
# Counter, namedtuple, OrderedDict, defaultdict, deque
# ---------------------------------------------------------

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# ---------------------------------------------------------
# Counter
# Counts occurrences of elements in iterable
# ---------------------------------------------------------

a = "aaaaaaaabbbbbccc"
my_counter = Counter(a)
print(my_counter)                # Counter({'a': 8, 'b': 5, 'c': 3})
print(my_counter.most_common(3)) # Top 3 most common elements
print(my_counter.items())        # All elements with counts
print(my_counter.keys())         # Only keys
print(my_counter.values())       # Only values
print(list(my_counter.elements()))  # Iterator of elements repeated

# ---------------------------------------------------------
# namedtuple
# Lightweight object type for named fields
# ---------------------------------------------------------

Point = namedtuple("Point", "x y")
pt = Point(1, -4)
print(pt.x, pt.y)   # Access fields by name

# ---------------------------------------------------------
# OrderedDict
# Preserves the order in which keys are added
# ---------------------------------------------------------

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

# ---------------------------------------------------------
# defaultdict
# Returns default value if key is missing
# ---------------------------------------------------------

d = defaultdict(int)  # Default is 0
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['g'])         # Key 'g' does not exist → prints 0

# ---------------------------------------------------------
# deque
# Double-ended queue, efficient for appending/popping from both ends
# ---------------------------------------------------------

dq = deque()
dq.append(1)          # Add to right
dq.appendleft(5)      # Add to left
print(dq)

dq.pop()               # Remove from right
print(dq)

dq.popleft()           # Remove from left
print(dq)

dq.extend([4,5,6])    # Add multiple elements to right
print(dq)

dq.extendleft([7,8,9]) # Add multiple elements to left (reversed order)
print(dq)

dq.rotate(2)           # Rotate elements to the right
print(dq)

# ---------------------------------------------------------
# ITERTOOLS IN PYTHON
# product, permutations, combinations, accumulate, groupby
# repeat, cycle, count
# ---------------------------------------------------------

from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import accumulate, groupby, count, cycle, repeat
import operator

# ---------------------------------------------------------
# product
# Cartesian product of input iterables
# repeat=n → repeat the iterable n times
# ---------------------------------------------------------

a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)
print(list(prod))
# Step by step:
# repeat=2 → consider the input as (a,b,a,b)
# Output: tuples of every possible combination in order

# ---------------------------------------------------------
# permutations
# All possible orderings of elements
# ---------------------------------------------------------

a = [1, 2, 3]
perm = permutations(a)   # Length defaults to full list
print(list(perm))

# ---------------------------------------------------------
# combinations
# Unique combinations without replacement
# ---------------------------------------------------------

a = [1, 2, 3, 4]
comb = combinations(a, 2)  # Pick 2 at a time
print(list(comb))

# ---------------------------------------------------------
# combinations_with_replacement
# Combinations allowing repeated elements
# ---------------------------------------------------------

comb = combinations_with_replacement(a, 2)
print(list(comb))

# ---------------------------------------------------------
# accumulate
# Running totals or other binary functions
# ---------------------------------------------------------

a = [1, 2, 3, 4]

# Sum
acc = accumulate(a)
print(list(acc))  # [1, 3, 6, 10]

# Multiplication
acc = accumulate(a, func=operator.mul)
print(list(acc))  # [1, 2, 6, 24]

# Max
acc = accumulate(a, func=max)
print(list(acc))  # [1, 2, 3, 4]

# ---------------------------------------------------------
# groupby
# Groups consecutive elements by key function
# ---------------------------------------------------------

def bigger_than_3(x):
    return x > 3

a = [1, 2, 3, 4]
group = groupby(a, key=bigger_than_3)
for key, value in group:
    print(key, list(value))  # key = True/False, value = group iterator

# ---------------------------------------------------------
# Infinite iterators: count, cycle, repeat
# ---------------------------------------------------------

# count(start) → infinite counting
# WARNING: infinite loop if you don't break
# for i in count(10):
#     print(i)

# cycle(iterable) → repeat the iterable infinitely
# for i in cycle([1,2,3]):
#     print(i)

# repeat(element, times) → repeat element finite or infinite
for i in repeat(1, 4):
    print(i)   # prints 1 four times
