class Contact:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

        self.validate_name()
        self.validate_email()
        self.validate_age()

    def validate_name(self):
        if len(self.name) > 50:
            raise ValueError('Name is too large!')

    def validate_email(self):
        if '@' not in self.email or '.' not in self.email:
            raise ValueError('Invalid email!')

    def validate_age(self):
        try:
            age = int(self.age)
            if age <= 0:
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

    def __repr__(self):
        return f"Contact(name= {self.name}, email= {self.email}, age= {self.age})"