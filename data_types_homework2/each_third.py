# 3, 2, 1, 4, 5,  2, ss, q
# ['3', '1', '5', 'ss']

sequence = "3  ,  2,   1, 4, 5,  2, ss  , q"
items = sequence.split(", ")
print(items)
stripped_elements = [item.strip() for item in items]   # list comprehension
stript_elem2 = []
for item in items:
    stript_elem2.append(item.strip())

print(stripped_elements)

result = stripped_elements[::2]

print(result)