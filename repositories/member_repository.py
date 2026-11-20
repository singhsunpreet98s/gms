from repositories.json_repository import JsonRepository;

class MemberRepository(JsonRepository):
    def __init__(self):
        super().__init__("members")