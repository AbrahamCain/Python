#keyScrape() takes in a dictionary of dictionaries and provides the keys
# associated with the top-level dictionary in a string so that items may
# may be iterrated within the dictionaries.
def keyScrape(data):
    #Define unneeded characters
    ls = [')', '(', '[', ']', "'"]
    
    #Grab the dict keys into a string excluding the first 11 characters
    string=str(data.keys())[10:]
    
    #Take out the other unneeded characters
    for i in ls:
        string = string.replace(i,"")
        
    #Make the key string a list for easy management    
    string = list(string.split(", "))
    
    return string
