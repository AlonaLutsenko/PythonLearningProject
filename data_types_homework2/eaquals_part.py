# 3, 2, 1, 4, 5,  2, ss, q
# ['3', ' 2', ' 1', ' 4'] [' 5', '  2', ' ss', ' q']

sequence = "3, 2, 1, 4, 5,  2, ss, q"
elements = sequence.split(',')

mid_ind = len(elements)//2


print(elements[:mid_ind], elements[mid_ind:])
