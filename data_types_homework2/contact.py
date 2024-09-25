# Enter your name: Nick
# Enter your age: 23
# Enter your address: Kiev, Ukraine
# Enter your phone: 0670000000
# Output: Contact created: {'name': 'Nick', 'age': 23, 'address': 'Kiev, Ukraine', 'phone': '0670000000'}

name  = input("Enter your name: ")
age  = input("Enter your age: ")
address  = input("Enter your address: ")
phone  = input("Enter your phone: ")

contact_info = {"name": name, "age": age, "address": address, "phone": phone}

print(f"Contact created: {contact_info}")