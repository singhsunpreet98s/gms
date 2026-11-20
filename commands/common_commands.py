class CommonCommands:

    @staticmethod
    def add_member(container):
        name = input("Enter name : ");
        phone = input("Enter Phone : ");

        container.member_service.add(name,phone);

    @staticmethod
    def list_members(container):
        members = container.member_service.get_all();
        for member in members :
            print("#"*20);
            print(f"Id : {member['id']}");
            print(f"Name : {member['name']}");
            print(f"Phone : {member['phone']}");

    @staticmethod
    def add_membership(container):

        member_id = input("please enter member Id : "); 
        plan_id = input("please enter plan Id : ")
        start_date = input("please enter start date DD-MM-YYYY : ")
        end_date = input("please enter end date DD-MM-YYYY : ");

        container.membership_service.add(member_id,plan_id,start_date,end_date);

    @staticmethod
    def list_memberships(container):
        memberships = container.membership_service.get_all();
        for membership in memberships:
            print("#"*20);
            print(f"Id : {membership['id']}");
            print(f"Start Date : {membership['start_date']}");
            print(f"End Date : {membership['end_date']}");
