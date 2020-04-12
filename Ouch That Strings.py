#welcome to "Ouch, That Strings!"

string = input("Please enter a phrase to play around with---->")
string += "."
print("Our String is:")
print(string, "\n\n")
input("\t\tPress ENTER to continue\n\n")

#center the string with +'s for padding
print("Here it is with the .center module:")
print(string.center(100, "+"), "\n")
input("\t\tPress ENTER to continue\n\n")

#count number of occurances
print("Here it is with the .count module to count the occurances of letter e:")
print(string.count("e"), "\n\n")
input("\t\tPress ENTER to continue\n\n")

#tells whether it ends with...
print("and Here using the .endswith module:\n")
print('---------String ends with "Water Balloon"---------')
print(string.endswith("Water Balloon"))
print("\n")
print('---------String ends with "stringFun.py"---------')
print(string.endswith("."), "\n\n")
input("\t\tPress ENTER to continue\n\n")

#find the position in a string where something is referenced
if "e" in string:
    letter = string.find("e")
    alpha = "e"
    print('What is the first index in the string', alpha, 'is referenced?')
    print(letter, "\n\n")
elif "a" in string:
    letter = string.find("a")
    alpha = "a"
    print('What is the first index in the string', alpha, 'is referenced?')
    print(letter, "\n\n")
else:
    print("There aren't any E's or A's in your phrase.\n\n")
    
input("\t\tPress ENTER to continue\n\n")

#capitalize the string\
print("Here it is with the .capitalize module:")
print(string.capitalize(), "\n\n")
input("\t\tPress ENTER to continue\n\n")

#all lowercase
print("Here is the .lower module:")
print(string.lower(), "\n\n")
input("\t\tPress ENTER to continue\n\n")

#all caps
print("Here is the .upper module:")
print(string.upper(), "\n\n")
input("\t\tPress ENTER to continue\n\n")

#First letter of every word capitalized
print("Here is the .title module:")
print(string.title())
input("\t\tPress ENTER to continue\n\n")

#replace all occurances of string1 with string2
print("Here is the .replace module:")
print(string.replace("e", "3"))
input("\t\tPress ENTER to Exit\n\n")

exit(0)
