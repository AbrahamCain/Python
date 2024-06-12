import sys

def indent(filename, openSection, closeSection):
    
    file = open(filename, "r")
    previous = ""
    numIndent = 0

    for current in file:

        if (openSection in current and openSection in previous):
            numIndent += 1
        elif (closeSection in current and closeSection in previous):
            numIndent -= 1
        else:
            numIndent = numIndent
        
        print( "\t" * numIndent + current, end="")
        previous = current
    
try:
    indent(sys.argv[1], sys.argv[2], sys.argv[3])
except:
    print("""
          Usage:
          \tpython3 indent.py <fileName> <openSection> <closeSection>
          
          \tfilename      - This is the name of the file you want to read from
          \topenSection   - This is a string that will indicate this line should be the beginning of a section
          \tcloseSection  - This is a string that will indicate this line should be the end of a section
          
          
          Example:
          \tpython3 indent.py unIndented.xml \"<tag\" \"</tag\"
          """)