# Input: 1, 2, 11 ,1  , 2, 2, 3
# Unique: 1, 2, 3, 11

sequence = "1,   2,   11 ,1  , 2, 2  , 3"
numbers = [int(num.strip()) for num in sequence.split(',')]
#print(numbers, id(numbers))

sorted_numbers = sorted(set(numbers))
print(sorted_numbers, id(sorted_numbers))

frozen_sorted_numbers = sorted(frozenset(numbers))
print(frozen_sorted_numbers, id(sorted_numbers))