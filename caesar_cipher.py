print("HELLO AND WELCOME TO THE CAESAR CIPHER!!!!\n")


cipherText = input("Ciphertext: ").lower()


#print all options and keep shifting the cipher
shift = 0
while shift < 26:

    decoded = []
    
    #decode the message
    for i in cipherText:
        
        #skip non-alpha characters
        if i.isalpha():

            num1 = ord(i) + shift
        
            if num1 > ord('z'):
                over = (num1 - ord('z')) + 96
                decoded.append(chr(over))
            elif num1 < ord('z'):
                decoded.append(chr(num1))
            elif num1 == ord('z'):
                decoded.append(chr(num1))
            else:
                print("\nSomething Went Wrong")
        else:
            decoded.append(i)

    #display message
    print("".join(decoded), "\t\tShifted {} Times".format(shift))

    #shift and itterate
    shift = shift + 1
