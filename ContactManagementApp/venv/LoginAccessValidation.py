import UserInfo
class LoginAccessValidation:
    """A class interface for validation of Login Access """
    def __init__(self,name):
        """Constructor for LoginAccessValidation"""
        self.name=name
        self.token=1200
        self.activeUserList=[]
        self.activeTokenList=[]
    def accessValidation(self,username,password):
        """Validates access for the user corressponding to the password and generates access token"""
        userOb = UserInfo.UserInfo
        found = 0
        self.accessTokenList = {}
        userPrevilege =-1
        for (i, j) in userOb.users:
            if (i == username and j == password):
                found = 1
                break
        if (found == 0):
            return  False # wrong username or password

        # generating token
        #self.accessTokenList[username] = self.token
        self.activeUserList.append(username)
        self.activeTokenList.append(self.token)
        self.userPrevilege = userOb.userPrevilege
        self.userFlags=userOb.userFlags
        self.token += 1
        return True


# def accessValidation(username,password,userPrevilege):
#     """Validates access for the user corressponding to the password and generates access token"""
#     userOb=UserInfo.UserInfo
#     found=0
#     accessTokenList = {}
#     token = 1200
#     userPrevilege=-1
#     for (i,j) in userOb.users:
#         if(i==username and j==password):
#             found=1
#             break
#     if(found==0):
#         return (0,userPrevilege) # wrong username or password
#
#     #generating token
#     accessTokenList[username]=token
#     userPrevilege=userOb.userPrevilege[username]
#     token+=1
#     return (accessTokenList,userPrevilege)

