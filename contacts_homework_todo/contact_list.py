from contact import Contact

class ContactList:
    def __init__(self):
        self.contacts = []

    def append(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError('Invalid contact! Must be an instance of Contact.')
        self.contacts.append(contact)

    def __iter__(self):
        return iter(self.contacts)

