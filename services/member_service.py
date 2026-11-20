from repositories.member_repository import MemberRepository;
from models.member import Member;

class MemberService:
    def __init__(self):
        self.member_repo = MemberRepository();

    def add(self, name, phone):
        self.member_repo.add(Member(name,phone));
        self.member_repo.save();

    def get_all(self):
        return self.member_repo.get_all();
