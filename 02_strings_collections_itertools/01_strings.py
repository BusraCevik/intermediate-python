# ---------------------------------------------------------
# STRINGS IN PYTHON
# Ordered, immutable, text representation
# ---------------------------------------------------------
# Strings are sequences of characters.
# They are ordered (indexable) but immutable (cannot be changed).
# ---------------------------------------------------------

my_string = "Hello"
print(my_string)

# ---------------------------------------------------------
# MULTI-LINE STRINGS
# ---------------------------------------------------------

my_string = """Hello
World"""
print(my_string)   # Writes on two lines

my_string = """Hello\
World"""
print(my_string)   # Line continuation, stays on one line

# ---------------------------------------------------------
# INDEXING
# ---------------------------------------------------------

my_string = "Hello World"
char = my_string[0]     # First character
print(char)

char = my_string[-1]    # Last character
print(char)

# ---------------------------------------------------------
# IMMUTABILITY
# ---------------------------------------------------------
# Strings cannot be changed character by character.
# This will raise an error:
'''
my_string = "Hello World"
my_string[0] = 'h'   # ERROR → strings do not support item assignment
'''

# ---------------------------------------------------------
# SLICING
# ---------------------------------------------------------

my_string = "Hello World"
substring = my_string[1:3]   # Characters at index 1 and 2 → 'el'
print(substring)

# ---------------------------------------------------------
# CONCATENATION
# ---------------------------------------------------------

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# ---------------------------------------------------------
# ITERATION
# ---------------------------------------------------------

for char in greeting:
    print(char)

# ---------------------------------------------------------
# MEMBERSHIP
# ---------------------------------------------------------

if 'e' in greeting:
    print('yes')
else:
    print('no')

# ---------------------------------------------------------
# STRING METHODS
# ---------------------------------------------------------

my_string = '  Hello World  \n'
my_string = my_string.strip()     # Removes leading/trailing spaces + \n
print(my_string)

print(my_string.lower())           # Lowercase
print(my_string.upper())           # Uppercase
print(my_string.startswith('Hello'))
print(my_string.endswith('Hello'))  # False → ends with "World"

print(my_string.count('Hello'))     # Count occurrences
print(my_string.find('lo'))         # First index or -1

print(my_string.replace('World', 'Universe'))  # Replace text

# ---------------------------------------------------------
# SPLIT & JOIN
# ---------------------------------------------------------

my_string = "How are you doing"
my_list = my_string.split(" ")     # Split by space
print(my_list)

new_string = ''.join(my_list)       # Join without spaces
print(new_string)

# ---------------------------------------------------------
# PERFORMANCE: LOOP CONCAT vs JOIN
# ---------------------------------------------------------

my_list = ['a']
print(my_list)

from timeit import Timer as timer
# Bad performance (creates new string each iteration)
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

# Good performance (efficient join)
start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop - start)

# ---------------------------------------------------------
# STRING FORMATTING
# ---------------------------------------------------------

# 1) % formatting (old style)
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 12
my_string = "the variable is %d" % var
print(my_string)

var = 12.12
my_string = "the variable is %f" % var
print(my_string)

# 2) .format() (modern)
var = 12.12454564
var2 = 6
my_string = "the variable is {:.2f}, {}".format(var, var2)
print(my_string)

# 3) f-strings (cleanest and best in modern Python)
var = 12.12454564
var2 = 6
my_string = f"the variable is {var}, {var2}"
print(my_string)
