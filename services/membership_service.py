from repositories.membership_repository import MembershipRepository;
from models.memebership import Membership;

class MembershipService:
    def __init__(self):
        self.membership_repo = MembershipRepository();

    def add(self,member_id,plan_id,start_date,end_date):
        self.membership_repo.add(Membership(member_id,plan_id,start_date,end_date,'Active','Complete'));
        self.membership_repo.save();

    def get_all(self):
        return self.membership_repo.get_all();