#Password Fancifier by Cyber_Surfer
#This program takes a cool word or phrase you like and turns it into a decent password

#you can comment out or delete the following 3 lines if using an OS other than Windows
import os
import sys
os.system("color e0") #It basically alters the colors of the terminal



#Enter a password and store it in the variable "word"
word = input("Give me a word/phrase to turn into a password of at least 10 characters please:\n\n--->")
word = word.lower()



#check the length of the password/phrase
count = len(word)
if count >= 10:
    for i in word:
        if "e" in word:
            word = word.replace("e", "3")   #replace e's with 3's
        if "a" in word:
            word = word.replace("a", "@")   #replace a's with @'s 
        if "s" in word:
            word = word.replace("s", "$")   #replace s's with $'s
            
    word = word.title()  #make the first letter of words uppercase

    #make 3 other options for passwords if the environment doesn't allow spaces, underscores, or dashes
    underscore = word.replace(" ", "_")
    tac = word.replace(" ",  "-")
    nospace = word.replace(" ", "")


    #print results
    print("Here are four different options:")
    print("1.",word)
    print("2.",underscore)
    print("3.",tac)
    print("4.",nospace)


#Let user know the password is too short
else:
    print("That password is too short. Try something over 10 characters next time.")



#End/Exit the program
input("Press ENTER To Exit")
exit(0)
