MaxIndex = 20
MyUserID = input("My user ID: ")
MyPassword = input("My password: ")
UserIdFound = False
LoginOK = False
Index = 0
while UserIdFound == False and Index != MaxIndex :
    Index += 1
    if UserList[Index] == MyUserID:
        UserIdFound = True
if UserIdFound == True and PasswordList[Index] == MyPassword:
    LoginOK = True
if LoginoOK == True:
    print("Login succesful")
else:
    print("User ID and/or passwrod incorrect")
