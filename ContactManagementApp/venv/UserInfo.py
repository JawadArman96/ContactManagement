
class UserInfo:
    users = [["jawad","okay123"], ["arman","clear123"],["ismam","pass123"]]
    userPrevilege={"jawad":1,"arman":2,"ismam":3}
    userFlags={1:"Admin",2:"Super",3:"Regular"}
    def __init__(self,name):
        """Constructor function for UserInfo class"""
        self.name=name
        self.admin="admin"
        self.super="super"
    def insertUser(self,employee,userFlag):
        """Insert user to the userlist"""
        print("Set the password for user")
        password=str(raw_input())
        self.users.append((employee.name,password))
        if(userFlag==1):
            print("Enter the privilege level\n3 for regular user")
        elif userFlag==2:
            print("Enter the privilege level\n3 for regular user\n2 for admin user")
        privilegeLevel=int(raw_input())
        self.userPrevilege[employee.name]=privilegeLevel
    def removeUser(self,employee,userflag):
        """"Remove user from the user list"""
        self.users.remove((employee.name,password))
        del self.userPrevilege[employee.name]
    def showUserList(self):
        """Show the list of users"""
        print("Users")
        print(self.users)
        print("User Privilege")
        print(self.userPrevilege)