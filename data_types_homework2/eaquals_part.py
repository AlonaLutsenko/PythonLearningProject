# 3, 2, 1, 4, 5,  2, ss, q
# ['3', ' 2', ' 1', ' 4'] [' 5', '  2', ' ss', ' q']

sequence = "3, 2, 1, 4, 5,  2, ss, q"
items = sequence.split(',')
stripped_elements = [item.strip() for item in items]
print(stripped_elements)

middle_index = len(stripped_elements) // 2
print(stripped_elements[:middle_index], stripped_elements[middle_index:])





# first_part = slice(0, 4)
# second = slice(4, len(stripped_elements))
# print(stripped_elements[first_part], stripped_elements[second])