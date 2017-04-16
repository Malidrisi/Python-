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
    d= {}
    flag = False
    for line in myfile:
        words=line.split()
        if len(words) > 0 and words[0] == "From:":
            d[words[1]]= d.get(words[1], 0) +1
            flag = True
        else:
            continue
    max = 0
    maxEmail = None 
    for key in d:
        if max == 0 or max < d[key] :
            maxEmail = key
            max = d[key]
            
if flag == True:
    print "The email address that sent the most emails is: " , maxEmail
    print "The number of emails sent from this email is: ", max
else:
    print "The file contains no relevant From: lines"
