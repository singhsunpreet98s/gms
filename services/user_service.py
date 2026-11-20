from repositories.user_repository import UserRepository;
from models.user import User;
class UserService:
    def __init__(self):
        self.user_repo = UserRepository();

    def add_user(self,name,email,password,role):
        self.user_repo.add(User(name,email,role,password))
        self.user_repo.save();

    def print_all(self):
        users = self.user_repo.get_all();
        for user in users:
            print("#"*20);
            print(f"Id : {user['id']}");
            print(f"Name : {user['name']}");
            print(f"Email : {user['email']}");