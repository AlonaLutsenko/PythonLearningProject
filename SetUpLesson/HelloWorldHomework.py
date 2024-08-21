# Just print Hellow world!
print('Hello world!\n')

# Print personal info
mySurname = 'Lutsenko'
myName = 'Alona'
myAge = 28
myInfo = mySurname + ' ' + myName + ' ' + str(myAge)
print('My personal info - ' + myInfo + '\n')
print(" ".join([myName, mySurname]) + "\n")

# Print multiple strings
multiple_string = '''First line: Never miss a good opportunity to shut up
Second line: If at first you don’t succeed, skydiving is not for you
Third line: Always borrow money from a pessimist
Fourth line: Don't take life too seriously\n'''
print(multiple_string)

# Formatted Print
print(f"Hi, my name is {myName} and I'm {myAge} years old.\n")

