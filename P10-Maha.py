# Author: Maha Alidrisi
import sys
import os
import re
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
    lst =[]
    for line in myfile:
        lst = lst + re.findall("New Revision: ([0-9]+)",line)
    if len(lst) > 0 :
        total= sum(float(n) if n else 0 for n in lst)
        length= sum(1 if n else 0 for n in lst)
        average= float(total/length)
        print "Average = ", format(average,'.1f')
        print "Number of lines = ", len(lst)
    else:
        print "The file contains no relevant New Revision lines"