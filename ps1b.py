# Program that computes the sum of the logs of all primes from 2 to n
from math import *

n = int(raw_input('Enter a number: '))
logsum = log(2)
testnumber = 3  # Starting with 3. 2 skipped
divisor = 2
isprime = True

while(testnumber<=n):
    while(divisor < testnumber/2):  # We only need to test divisors upto num/2
        if(testnumber%divisor == 0):
            isprime = False  
            break  # If num is divisible by any number then skip rest
        divisor += 1
    if(isprime == True):
        logsum = logsum + log(testnumber)
    testnumber+=2
print 'Sum of log of primes is: ', logsum
