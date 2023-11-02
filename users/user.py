class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname 
        self.email = email
        self.password = password

    def register(self):
        return "Ok, let's register you in the system..."

    def identificar(self):
        return "Ok, identify yourself in the system..."