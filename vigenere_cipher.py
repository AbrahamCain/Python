#A cipher breaker for vigenere cipher
key = input("Enter Ciphertext: ").lower()
cipherText = input("Enter KeyWord: ").lower() 
decoded = []

#Make sure the key and cipher text are the same length
cnt = 0
if len(cipherText) < len(key):
    while len(key) > len(cipherText):
        cipherText = cipherText + cipherText[cnt]
        if cnt == len(cipherText):
            cnt = 0
        else:
            cnt = cnt + 1


cnt = 0
for i in cipherText:
    
    #make a easier to work with variable for both
    l1 = i
    l2 = key[cnt]
    
    #do the alphabet math
    if (ord(l2) > ord(l1)):
        l3 = chr(ord(l2) - ord(l1) + 97)
    elif(ord(l2) < ord(l1)):
        l3 = chr(ord('z') - (ord(l1) - ord(l2))+1)
    elif(ord(l1) == ord(l2)):
        l3 = chr(97)
    else:
        print("oops. something went wron...")
    
    #Add the decoded letter to the Decoded Message
    decoded.append(l3)

    #itterate
    cnt = cnt + 1

#Display the decoded message
print("".join(decoded))
