# P11 -  Maha Alidrisi 
import urllib2
import io
import  re
import sys
inputURL = raw_input("Please enter a URL: ")
try:
    url= urllib2.Request(inputURL,headers={'User-Agent': 'Safari/537.36'})
    res= urllib2.urlopen(url)
except ValueError as e:
    print "Error:", e
else:
    f=res.read()
    f = f.lower()
    lst = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",f)
    if len(lst) > 0:
        uniURL=[]
        for i in lst:
            if i not in uniURL:
                uniURL.append(i)
    print "Total distinct http/https references: ", len(uniURL)
