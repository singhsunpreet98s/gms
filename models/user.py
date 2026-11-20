class User:
    def __init__(self, name, email, role, password):
        self.name = name;
        self.email = email;
        self.hash_password = password;
        self.role = role;
        self.is_active = True;


    