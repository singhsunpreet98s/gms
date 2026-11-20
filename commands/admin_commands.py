from commands.common_commands import CommonCommands;
import os;
class AdminCommand:
    def __init__(self,container):
        self.container = container;
    
    def run(self):
        print("Select one option");
        print("1. Add User");
        print("2. List all users")
        print("3. Add Member");
        print("4. List all memebers")
        print("5. Add Trainer");
        print("6. List all Trainers");
        print("7. Add Memebership");
        print("8. List all Memberships");
        print("9. Add Plan");
        print("10 List all plans");
        user_input = int(input("Tell me option number : "));
        self.user_action(user_input=user_input);

    def user_action(self, user_input):
        match user_input:
            case 1:
                self.add_user();
            case 2:
                self.list_users();
            case 3: 
                CommonCommands.add_member(self.container);
            case 4:
                CommonCommands.list_members(self.container);
            case 7:
                CommonCommands.add_membership(self.container);
            case 8:
                CommonCommands.list_memberships(self.container);
            case 9:
                self.add_plan();
            case 10:
                self.list_plans();
            case _:
                print("No option selected");


    def add_user(self):
        name = input("Please enter name : ");
        email = input("Please enter email : ");
        password = input("Please enter password : ");
        role = input("Please enter role : \n 1. Admin \n 2. User \n");

        self.container.user_service.add_user(name,email,password,role);
        print("user successfully added");

    def list_users(self):
        self.container.user_service.print_all();

    def add_plan(self):
        name = input("Enter plan name : ");
        duration = input("Enter plan duation : ");
        price = input("Enter plan price : ");
        desc = input("Enter plan description : ");

        self.container.plan_service.add(name,duration,price,desc);

    def list_plans(self):
        plans = self.container.plan_service.get_all();
        os.system("cls");
        print("#"*50);
        for plan in plans:
            print(f"Id : {plan['id']} ");
            print(f"Name : {plan['name']}");
            print(f"Duration : {plan['duration']} days");
            print(f"Description : {plan['desciption']}");
            print("-"*25);