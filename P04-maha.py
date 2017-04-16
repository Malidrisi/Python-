# Name: Maha Alidrisi
# This program generate random number between 1 - 20 and ask the user to guess the number. the user guesses are limited to 6 tries.

import random
import sys

attempts = 1
RandomNum = random.randint(1, 20)
name = raw_input("Hello! What is your name? ")
print "Well,", name,", I am thinking of a number between 1 and 20."

def guess(n,RandomNum):
    if n == RandomNum:
        return 0
    elif 0 < n < RandomNum:
        return -1
    elif 21 > n > RandomNum:
        return 1
    elif 0 > n or n > 20:
        return "error"
while attempts < 7:
    try:
        n = int(input("Take a guess: "))
    except:
        print "Please enter a number"
        sys.exit()   
    result= guess(n,RandomNum)    
    if result == 0 :
        print "Good job,", name,"! You guessed my number in ",attempts," guesses! " ,RandomNum
        break
    elif result == -1:
        print "Your guess is too low"
        attempts = attempts+1
    elif result == 1:
        print "Your guess is too high"
        attempts = attempts+1
    elif result == "error":
        print "Please enter a number between 1 and 20"
         
if n != RandomNum:
    print "The number I was thinking of was", RandomNum