# Input: 3, 2, 1, 4, 5,  2
# Output: [1, 2, 2, 3, 4, 5]

numbers = 3, 2, 1, 4, 5,  2
sorted_numbers = sorted(numbers)
sorted_numbers_reverse = sorted(numbers, reverse=True)

print("Sorted numbers: ", sorted_numbers)
print("Sorted numbers desc:", sorted_numbers_reverse)





print(numbers, id(numbers), type(numbers)) # list
# print(sorted_numbers, id(sorted_numbers)) # new list
# print(sorted_numbers_reverse, id(sorted_numbers_reverse)) # new list