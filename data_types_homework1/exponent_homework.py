import math

x = 3
print(x, id(x))
x = 7
print(x, id(x))

y = 2
exp = math.pow(x, y)
print(int(exp))

# or
print(pow(x, y))

# or
print(x**y)