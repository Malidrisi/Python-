# -*- coding: utf-8 -*-
# Author: Maha Alidrisi
import sys
import os
import string
from operator import itemgetter

fName =  raw_input("Enter the file name: ")
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
    words= {}
    chars= {}
    for line in myfile:
        line = line.translate(None,string.punctuation)
        line = line.lower()
        l = line.split()
        for word in l:
            words[word]= words.get(word, 0)+ 1
            result = ''.join(i for i in word if not i.isdigit())
            for ch in result.strip(): 
                chars[ch] = chars.get(ch,0) + 1

    #sort dict words by key         
    sW = sorted(words.items(),key=itemgetter(1), reverse=True)
    #sort dict chars by key 
    sCH = sorted(chars.items(),key=itemgetter(1), reverse=True)

    print "This file has", sum(words.itervalues()), "words and", len(words), "distinct words"
    
    print "\nThe top 25 most frequent words and counts are:\n", 
    for k,v in sW[:25]:
        print k,"- appears" ,v,"times"
        
    print "\nThe character frequencies in this file are:"
    for k,v in sCH:
        print k,"- appears" ,v,"times"    