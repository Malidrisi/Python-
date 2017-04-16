# Author: Maha Alidrisi
import sys
import os
fName = raw_input("Enter the file name: ")
try: 
    myfile= open(fName)
    if os.stat(fName).st_size == 0:
        raise Exception
except IOError:
    print "File",fName, "does not exist"
    sys.exit()  
except Exception:
    print "File",fName,"is empty"
    sys.exit()  
else:
    count = 0
    total= 0.0
    for line in myfile:
        words=line.split()
        if len(words) > 0:
            if words[0] == "X-DSPAM-Confidence:":
                count =count +1
                try:
                    total= total + float(words[1])
                except ValueError:
                    print "ValueError: could not convert string to float"
                    sys.exit() 
            else:
                continue
        else:
            continue
    if count > 0:
        print "Average spam confidence:",format(total/count, '.4f')
    else:
        print "There is no -X-DSPAM-Confidence- in this file"