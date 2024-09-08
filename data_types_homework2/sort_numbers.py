numbers = 3, 2, 1, 4, 5,  2
sorted_numbers = sorted(numbers)
sorted_numbers_reverse = sorted(numbers, reverse=True)

print(sorted_numbers)
print(sorted_numbers_reverse)


print(numbers, id(numbers)) # list
print(sorted_numbers, id(sorted_numbers)) # new list
print(sorted_numbers_reverse, id(sorted_numbers_reverse)) # new list