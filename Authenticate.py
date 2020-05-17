#Authenticate 1.0
#A basic authentication program

count = 0

#Define a list of usernames and passwords
userList = ["Mark", "Sam", "Paul"]
passList = ["password", "admin", "test123"]

#Ask for a valid username contained in the userList
while (True):
    userAttempt = input("Username: ")
    if (userAttempt in userList):
        break    #if the username is valid, move on to the next check
    else:
        print("Invalid Username")
        continue #if the username is not valid, keep asking for a username


#Ask for a valid password contained in passList
while (True and count < 5): #mitigate brute forcing by allowing 5 attempts before exiting

    #Exit if there are too many attempts, terminate the program
    if (count == 3):
        input("Too Many Invalid Entries!!!\nGoodbye")
        exit()
        
        
    passAttempt = input("Password: ")
    #Make sure password is in the passList
    if (passAttempt in passList):
        
        #Make sure the username corresponds with the right account
        if (passList.index(passAttempt) == userList.index(userAttempt)):
            break
        else:
            print("\nIncorrect Password\n")
            count += 1
            continue
    else:
        count += 1
        continue


input("Welcome ", userAttempt, ". You have been logged in.")
