#my basic dashboard CLI for opening tabs
#utilizes the following modules:
    #webbrowser.open(url, new=1,2, 0r 3)
    #time.sleep(# of seconds)


import webbrowser
import time
import sys
import os

#adust cmd.exe colors
os.system("color 3")
tabs = []
end = False

#display options
print("""
Here is a list of websites I can open up for you:
1. frederick.blackboard.com
2. hackthebox.eu
3. bugcrowd.com
4. netacad.com
5. overthewire.org
6. Other
""")

#make a loop to determine how many tabs are needed

done = "NO"
while done == "NO":
    num = int(input("How many tabs do you need?:\t"))
    done = input("Are you sure? YES or NO:\t")
    done = done.upper()

    if done == "YES" or done == "Y":
       break
    else:
       None

#make a valid list of options
valid = [1,2,3,4,5,6]

for i in range(1, num++1):
    print("""
Here is a list of websites I can open up for you. Please select one of the following:
1. frederick.blackboard.com
2. hackthebox.eu
3. bugcrowd.com
4. netacad.com
5. overthewire.org
6. Other
""")
    option = int(input("Please present option as a single digit number---->"))
    #make sure option is valid and let them enter a URL if not
    if option not in valid:
        print("That isn't a valid option, so we chose 6 for you.")
        option = 6
    tabs.append(option)     #add the option to a list

#Start opening the tabs or if option 6, allow them to specify a URL
for i in tabs:
    
    if i ==  1:
        webbrowser.open("frederick.blackboard.com", new=1)
    elif i == 2:
        webbrowser.open("hackthebox.eu/login", new=1)
    elif i == 3:
        webbrowser.open("bugcrowd.com/user/sign_in", new=1)
    elif i == 4:
        webbrowser.open("netacad.com/saml_login", new=1)
    elif i == 5:
        webbrowser.open("overthewire.org", new=1)
    elif i == 6:
        url = str(input("Please enter the exact URL you would like to enter---->"))
        
        webbrowser.open(url, new=2)
    else:
        print("Something went wrong")

    time.sleep(5)   #add a 5 second delay to load pages

#end of program
input("Press ENTER To Exit")
exit(0)
