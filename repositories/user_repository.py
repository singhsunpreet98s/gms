from repositories.json_repository import JsonRepository;

class UserRepository(JsonRepository):
    def __init__(self):
        super().__init__("users");
