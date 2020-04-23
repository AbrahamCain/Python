import base64

option = input("Enter 1 for Encode or 2 for Decode----->")

if (option=="1"):
    #Encoding Section
    data = bytes(input(("Enter something to encode----->")), 'utf-8')
    coded = base64.b64encode(data)
    print(coded)
    input("press enter to Exit")
    exit(0)
elif (option=="2"):
    #Decoding Section
    data = input(b"Enter something to encode----->")
    decoded = base64.b64decode(data)
    print(decoded)
    input("press enter to Exit")
    exit(0)

else:
    print("That wasn't an option")

