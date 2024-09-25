# 3, 2, 1, 4, 5,  2, ss, q
# ['3', '1', '5', 'ss']

sequence = "3, 2, 1, 4, 5,  2, ss, q"
items = sequence.split(", ")
result = items[::2]
print(result)