from repositories.json_repository import JsonRepository;

class TrainerRepository(JsonRepository):
    def __init__(self):
        super().__init__("trainers");
