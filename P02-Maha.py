import sys;
x = raw_input('Please enter your score: ')
try:
    score= float(x)
except:
    print "Please enter numeric input."
    sys.exit()  
if 93 <= score <= 100: 
    print "Your grade is: A"
elif 90 <= score < 93: 
    print "Your grade is: A-"
elif 87 <= score < 90: 
    print "Your grade is: B+"
elif 83 <= score < 87: 
    print "Your grade is: B"    
elif 80 <= score < 83: 
    print "Your grade is: B-"  
elif 70 <= score < 80: 
    print "Your grade is: C"  
elif 0<= score <70: 
    print "Your grade is: F"
else:
    print "Please enter a score between 0 and 100"