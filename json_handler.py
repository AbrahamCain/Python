#keyScrape() takes in a dictionary of dictionaries and provides the keys
# associated with the top-level dictionary in a string so that items may
# may be iterrated within the dictionaries.

import json

def keyScrape(data):
    #Define unneeded characters
    ls = [')', '(', '[', ']', "'"]
    
    #Grab the dict keys into a string excluding the first 11 characters
    d = data.replace("\n","")
    d = json.loads(data)
    
    string=str(d.keys())[10:]
    
    #Take out the other unneeded characters
    for i in ls:
        string = string.replace(i,"")
        
    #Make the key string a list for easy management    
    string = list(string.split(", "))
    
    return string

def stringScrape(data):
    #Define unneeded characters
    ls = [')', '(', '[', ']', "'"]

    #Parse the key values out of the JSON Response String
    

    #Take out the other unneeded characters
    for i in ls:
        string = string.replace(i,"")
        
    #Make the key string a list for easy management    
    string = list(string.split(", "))
    
    return string
