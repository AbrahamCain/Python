import requests
#Uncomment below in version 2.0 to use the re library to use regular expressions instead of the .find() method
# import re

#GET request to the website
page=requests.get("https://www.tenable.com/security")

#Check for an HTTP status 400 or higher and 
if page.ok:
    print("GET went well")
else:
    print("Got an HTTP status >= 400 or some other error")
    exit(400)

pageAsString=str(page.content)

sIndex=pageAsString.find("<tbody>")
eIndex=pageAsString.find("</tbody>")

# Print start and end indexes of the table containing the advisories
#print(sIndex, " ", eIndex)

advisoryTable=pageAsString[sIndex:eIndex]


file=open("textFile.txt", 'w')
file.write(advisoryTable)
file.close()

print("Written to ./textFile.txt")

exit(0)
