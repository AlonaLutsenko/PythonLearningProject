from contact import Contact
from contact_list import ContactList

if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()

    while True:
        try:
            name = input('name: ')
            email = input('email: ')
            age = input('age: ')

            contact = Contact(name= name, email= email, age= age)

            contact_list.append(contact)

        except ValueError as e:
            print(e)
            continue

        proceed = input('add another one? (y/n): ')
        if proceed != 'y':
            break

    print("Contacts:")
    print(contact_list)
