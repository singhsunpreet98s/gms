from repositories.json_repository import JsonRepository;

class PlanRepository(JsonRepository):
    def __init__(self):
        super().__init__("plans");
