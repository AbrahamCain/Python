#myClip.py is a program that allows you to copy the contents of something to your clipboard based upon an option list
#this module isn't part of the standard library so uncomment the next 3 lines if you haven't installed pyperclip on Windows
#import os
#import sys
#os.system("pip install pyperclip")


import pyperclip

#You can add to or take away from this dictionary to change your options
#The keys will be the word you put after the command:
    #"python myClip.py <insertKeywordHere>"
#The values in triple quotes are what will be copied to your clipboard in the case of 
TEXT = {'agree' : """Yes, I agree. That sounds fine to me.""", 'busy': """Sorry, can we do this later this week or next week?""", 'upsell': """Would you consider making this a monthly donation?"""}

import sys
if (len(sys.argv) < 2):
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     #First Command line arg is keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
    
    
#For even easier use, make a .bat file named clip.bat in the C:\Windows directory that contains the following:
  #@python <Path to your myClip.py program here>
  #@pause

#This will allow you to launch your myClip from the run menu (WinKey+R) with the command "clip.bat <your option here>"

