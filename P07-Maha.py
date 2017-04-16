# Author: Maha Alidrisi
import sys
import os
fName = raw_input("Enter the file name: ")
try: 
    myfile= open(fName)
    if os.stat(fName).st_size == 0:
        raise Exception
except IOError:
    print "The file does not exist"
    sys.exit()  
except Exception:
    print "The file is empty"
    sys.exit()  
else:
    UniSender=[]
    for line in myfile:
        words=line.split()
        if len(words) > 0 and words[0] == "From:":
            if words[1] in UniSender:
                continue
            else:
                UniSender=  UniSender + [words[1]]
        else:
            continue
    if len(UniSender) > 0:
        print  len(UniSender)
    else: 
        print "The file contains no relevant From: lines"
