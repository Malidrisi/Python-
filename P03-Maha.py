# this program defines a method that finds the max of three entered value

def MaxOfThree(x, y, z):
    Max = x
    if y > Max:
        Max = y    
    if z > Max:
        Max = z
    return Max

x = raw_input('Enter first value: ')
y = raw_input('Enter Second value: ')
z = raw_input('Enter third value: ')
try:
    a=float(x)
    b=float(y)
    c=float(z)
    print "\n The maximum off",x, y, z,"is", MaxOfThree(a, b, c)
except:
    print "\n The maximum of",x, y, z,"is", MaxOfThree(x, y, z)