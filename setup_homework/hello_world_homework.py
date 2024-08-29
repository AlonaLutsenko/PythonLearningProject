# Just print Hellow world!
print('Hello world!\n')

# Print personal info
my_surname = 'Lutsenko'
my_name = 'Alona'
my_age = 28
my_info = my_surname + ' ' + my_name + ' ' + str(my_age)
print('My personal info - ' + my_info + '\n')
print(" ".join([my_name, my_surname]) + "\n")

# Print multiple strings
multiple_string = '''First line: Never miss a good opportunity to shut up
Second line: If at first you don’t succeed, skydiving is not for you
Third line: Always borrow money from a pessimist
Fourth line: Don't take life too seriously\n'''
print(multiple_string)

# Formatted Print
print(f"Hi, my name is {my_name} and I'm {my_age} years old.\n")