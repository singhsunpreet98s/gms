class Student:
    _instance = None;
    def __init__(self):
        self.counter = 1;
    

    def __new__(cls):
        cls._instance = super().__new__(cls);
        return cls._instance;

    def add(self):
        self.counter += 1;

    def print(self):
        print(f"Countr is : {self.counter}")