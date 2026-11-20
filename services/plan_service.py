from repositories.plan_repository import PlanRepository;
from models.plan import Plan;

class PlanService:
    def __init__(self,plan_repo):
        self.plan_repo = plan_repo

    def add(self,name,duration,price,desc):
        self.plan_repo.add(Plan(name,duration,price,desc))
        return self.plan_repo.save();

    def get_all(self):
        return self.plan_repo.get_all();