#This program works with a list of dictionaries


##########DECLARE DICTIONARY LIST##########

people = [{'name': 'Gandalf', 'style': 'Mage', 'age': '2000000'}, {'name': 'Sauron', 'style': 'Mage', 'age': '3000000'}, {'name': 'Frodo', 'style': 'Ring-Bearer', 'age': '18'}, {'name': 'Gollum', 'style': 'Thief', 'age':  '2000'}]


#############LOOP BODY 1################
i = 0
for l in people:

    label = i + 1
    print(("Character_" + str(label)).center(31, '=')) #decorative banners above the different characters with Character and the character number

    #######################LOOP BODY 2#########################
    for k, j in people[i].items():      #second loop for items in the dictionary
        print(k.ljust(20, '.') + j.rjust(11, '.'))  #prints the dictionary key and the key value separated by dots with a total width of 31 characters

    i+=1   #move on to the next dictionary by increasing the "i" value
    print('\n')
