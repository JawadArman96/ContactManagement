import LoginAccessValidation
import UserInfo
import UserAction
class LoginAction:
    def __init__(self,name):
        self.name=name
        self.username="NULL"
        self.password="NULL"
        self.userInfoOb=UserInfo.UserInfo("User")
    def showActiveStatus(self,loginOb):
        """Showing the access token for active users"""
        print("Active Status...")
        l = len(loginOb.activeUserList)
        for i in range(l):
            print(loginOb.activeUserList.__getitem__(i) + " " + str(loginOb.activeTokenList.__getitem__(i)))

    def userLogin(self):
        """Provides userinterface for User to login and call LoginAccessValidation function"""
        loginOb = LoginAccessValidation.LoginAccessValidation("LogInAccess")
        self.userActionOb = UserAction.UserAction("this")
        while True:
            print("Enter the username:")
            self.username = str(raw_input())
            print("Enter password:")
            self.password = str(raw_input())
            userPrevilege = -1
            boolValue = loginOb.accessValidation(self.username, self.password)
            # if len(loginOb.activeUserList)==0:
            if boolValue == False:
                print("Wrong username or password")
                continue
            else:
                userOb = UserInfo.UserInfo
                #self.userActionOb = UserAction.UserAction("this")
                print("You are " + loginOb.userFlags[loginOb.userPrevilege[self.username]] + " user")
                # showActiveStatus(loginOb)
                if loginOb.userPrevilege[self.username]==1:
                    var=self.adminUser()
                    while(var==True):
                        var=self.adminUser()
                elif loginOb.userPrevilege[self.username]==2:
                    var = self.superUser()
                    while (var == True):
                        var = self.superUser()
                else:
                    var = self.regularUser()
                    while (var == True):
                        var = self.regularUser()
    def showActiveStatus(self,loginOb):
        """Showing the access token for active users"""
        print("Active Status...")
        l = len(loginOb.activeUserList)
        for i in range(l):
            print(loginOb.activeUserList.__getitem__(i) + " " + str(loginOb.activeTokenList.__getitem__(i)))

    def adminUser(self):
        """provides interface for admin user"""
        print("Enter 1 to insert")
        print("Enter 2 to update")
        print("Enter 3 to delete")
        print("Enter 4 to search")
        print("Enter 5 to exit")
        print("Enter 6 to view all")
        option = int(raw_input())
        if option == 1:
            employee = self.userActionOb.insertEmployee()
            self.userInfoOb.insertUser(employee, 1)
        elif option == 2:
            self.userActionOb.updateEmployee()
        elif option == 3:
            self.userActionOb.deleteEmployee()
        elif option == 4:
            emp=self.userActionOb.searchEmployee()
            if (emp.name == "NULL"):
                print("Employee not found")
            else:
                self.userActionOb.showEmployee(emp)
        elif option == 5:
            return False
        elif option == 6:
            self.userActionOb.showEmployees()
        return True

    def superUser(self):
        """provides interface for super user"""
        print("Enter 1 to insert")
        print("Enter 2 to update")
        print("Enter 3 to delete")
        print("Enter 4 to search")
        print("Enter 5 to exit")
        print("Enter 6 to view all")
        option = int(raw_input())
        if option == 1:
            employee = self.userActionOb.insertEmployee()
            self.userInfoOb.insertUser(employee, 1)
        elif option == 2:
            self.userActionOb.updateEmployee()
        elif option == 3:
            self.userActionOb.deleteEmployee()
        elif option == 4:
            emp = self.userActionOb.searchEmployee()
            if (emp.name == "NULL"):
                print("Employee not found")
            else:
                self.userActionOb.showEmployee(emp)
        elif option == 5:
            return False
        elif option == 6:
            self.userActionOb.showEmployees()
        return True
    def regularUser(self):
        """provides interface for regular user"""
        print("Enter 1 to search")
        print("Enter 2 to exit")
        print("Enter 3 to view all")
        option=int(raw_input())
        if option==1:
            emp = self.userActionOb.searchEmployee()
            self.userActionOb.showEmployee(emp)
        elif option==2:
            return False
        elif option==3:
            self.userActionOb.showEmployees()

        return True


# def showActiveStatus(loginOb):
#     """Showing the access token for active users"""
#     print("Active Status...")
#     l=len(loginOb.activeUserList)
#     for i in range(l):
#         print(loginOb.activeUserList.__getitem__(i)+" "+str(loginOb.activeTokenList.__getitem__(i)))
#
# def userLogin():
#     """Provides userinterface for User to login and call LoginAccessValidation function"""
#     loginOb=LoginAccessValidation.LoginAccessValidation("LogInAccess")
#     while True:
#         print("Enter the username:")
#         username=str(raw_input())
#         print("Enter password:")
#         password=str(raw_input())
#         userPrevilege=-1
#         boolValue=loginOb.accessValidation(username,password)
#         # if len(loginOb.activeUserList)==0:
#         if boolValue==False:
#             print("Wrong username or password")
#             continue
#         else:
#             userOb=UserInfo.UserInfo
#             userActionOb=UserAction.UserAction("this")
#             print("You are "+loginOb.userFlags[loginOb.userPrevilege[username]]+" user")
#             #showActiveStatus(loginOb)
#             adminUser(userActionOb)

# def adminUser(userActionOb):
#     """provides interface for admin user"""
#     print("Enter 1 to insert")
#     print("Enter 2 to update")
#     print("Enter 3 to delete")
#     print("Enter 4 to search")
#     print("Enter 5 to exit")
#     option = int(raw_input())
#     if option == 1:
#         userActionOb.insertEmployee()
#     elif option == 2:
#         userActionOb.updateEmployee()
#     elif option == 3:
#         userActionOb.deleteEmployee()
#     elif option == 4:
#         employee=userActionOb.searchEmployee()
#         userActionOb.showEmployee()
#     elif option == 5:
#         username = "NULL"
#         password = "NULL"
# def superUser(userActionOb):
#     """provides interface for super user"""
#     print("Enter 1 to insert")
#     print("Enter 2 to update")
#     print("Enter 3 to delete")
#     print("Enter 4 to search")
#     print("Enter 5 to exit")
#     option = int(raw_input())
#     if option == 1:
#         userActionOb.insertEmployee()
#     elif option == 2:
#         userActionOb.updateEmployee()
#     elif option == 3:
#         userActionOb.deleteEmployee()
#     elif option == 4:
#         emp=userActionOb.searchEmployee()
#         userActionOb.showEmployee(emp)
#     elif option == 5:
#         username = "NULL"
#         password = "NULL"
#
# def regularUser():
#     """provides interface for regular user"""
#     emp = userActionOb.searchEmployee()
#     userActionOb.showEmployee(emp)

# a=[["abb","123"]]
# a.append(("abba","123"))
# print(a)
logob=LoginAction("this")
logob.userLogin()