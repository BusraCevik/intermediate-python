# 🟢 Lambda Functions: Small, one-line functions
# Syntax: lambda arguments: expression

# 🔹 Normal function vs lambda function
'''
def add10_func(x):
    return x + 10

print(add10_func(5))  # 5 + 10 = 15
'''

# 🔹 Same function using lambda
add10 = lambda x: x + 10
print(add10(5))  # 5 + 10 = 15

# 🔹 Lambda function that multiplies two numbers
mult = lambda x, y: x * y
print(mult(5, 2))  # 5 * 2 = 10

# 🔹 List of 2D points
points2d = [(7, 2), (3, 4), (10, 6)]

# 🔹 sorted() by default sorts by the first element (x coordinate)
points2d_sorted = sorted(points2d)
print("Original list:", points2d)
print("Sorted by x:", points2d_sorted)

# 🔹 Sorting points by the second element (y coordinate) using lambda
points2d_sorted = sorted(points2d, key=lambda p: p[1])
print("Original list:", points2d)
print("Sorted by y:", points2d_sorted)
