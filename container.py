class Container:
    def __init__(self):
        from repositories.member_repository import MemberRepository;
        from repositories.membership_repository import MembershipRepository;
        from repositories.plan_repository import PlanRepository;
        from repositories.user_repository import UserRepository;
        from repositories.trainer_repository import TrainerRepository;
        from services.user_service import UserService;
        from services.member_service import MemberService;
        from services.membership_service import MembershipService;
        from services.plan_service import PlanService;


        self.member_repo = MemberRepository();
        self.membership_repo = MembershipRepository();
        self.plan_repo = PlanRepository();
        self.trainer_repo = TrainerRepository();
        self.user_repo = UserRepository();
        self.user_service = UserService();
        self.plan_service = PlanService(self.plan_repo);  
        self.membership_service = MembershipService();
        self.member_service = MemberService();
