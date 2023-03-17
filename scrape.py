import requests, re

#So we can know that the program started and imports didn't crash
print('beginning')


##################################### INITIAL WEB SCRAPE (ADVISORY LIST) ######################################################


#Make a GET request to Tenable's Security Advisory page
page=requests.get("https://www.tenable.com/security")

#Check to ensure that the HTTP status code in the response is less
    #than 400
if page.ok:
    print("GET went well")
else:
    print("Got an HTTP status >= 400 or some other error")
    exit(400)

#Convert the webpage content from an array of bytes to a string
pageAsString=str(page.content)


#Use Builtin methods of the string to find the first occurances
    #of each string that opens and closes the body of the table
    #in the HTML document
sIndex=pageAsString.find("<tbody>")
eIndex=pageAsString.find("</tbody>")

# Print start and end indexes of the table containing the advisories
#print(sIndex, " ", eIndex)

advisoryTable=pageAsString[sIndex:eIndex]


#Uncomment below multi-line comment to store the table for offline access
"""file=open("textFile.html", 'w')
file.write(advisoryTable)
file.close()

print("Written to ./textFile.html")
"""


################################### SECOND LAYER WEB SCRAPE (ADVISORY CONTENT) ################################################


#Use REGEX to pull the security Advisory links out of the table
patternList=re.findall("href=\"/security/tns\-[0-9]{4}\-[0-9]{1,4}", advisoryTable)

#A combined list of affected products across all advisories
grandProductList=[]

#Iterate through the links
for link in patternList:

    #Uncomment below for some extra debugging 
    """
    print(link)
    url="https://www.tenable.com"+(str(link[6:]))
    print(url)
    """

    #Follow the links
    subPage=requests.get(("https://www.tenable.com"+(str(link[6:]))))

    #Start by testing to make sure that the page loads okay
    if subPage.ok:

        #Scrape the multi-line Affected Products fields from the page
            # and add them to the grand list
        #Adding a third field "re.DOTALL" to the re.search() function allows
            # the "." character to represent any character INCLUDING newlines
        try:
            affected=re.search(
                "affected\-products.*?          </div>",
                subPage.text,
                re.DOTALL).group()
            grandProductList.append(affected)

        #Print a note for any page without affected products 
        except:
            print("No Affected Products Field for:\t",subPage.request.url)

#Print the entries from the combined list to the terminal
for entry in grandProductList:
    print(re.findall(">.*?</", entry))
        

