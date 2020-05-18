#A program to create, write to, and read from text files
#Replace 'textFile.txt' in the open() modules to change the title of the file
#Replace 'a' in the 1st open() module with 'w' if you want the contents of the file
    #to be overwritten. This will open the file in write mode




    #Enter something to put into your file
words = input("Enter what you would like to put into your text file:\n-->")

    #Open the file in "append mode" (a) so you can add to the file
file = open('textFile.txt', 'a')

        #write the contents of the variable "words" to the file followed by a newline
file.write(words)
file.write("\n")

    #close the file
file.close()

    #open the file again but this time in "read mode" (r)
file = open('textFile.txt', 'r')

        #print the contents of the file to the console
print(file.read())

    #close the file
file.close()
