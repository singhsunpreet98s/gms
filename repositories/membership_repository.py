from repositories.json_repository import JsonRepository;

class MembershipRepository(JsonRepository):
    def __init__(self):
        super().__init__("memberships");
