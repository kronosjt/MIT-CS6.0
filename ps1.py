# Program that prints the 1000th prime number

# First generate all the odd integers>1 as candidates
# we can discard all the even numbers greater than 2

prime_counter = 0  # Counter for prime numbers found
number = 3  # Starting with 3. 2 skipped

while(prime_counter < 10000):
    divisor = 2
    isprime = True
    while(divisor < number/2):  # We only need to test divisors upto num/2
        if(number%divisor == 0):
            isprime = False  
            break  # If num is divisible by any number then skip rest
        divisor += 1
    if(isprime == True):
        prime_counter+=1
    if(prime_counter == 10000):
        print '1000th prime number: ', number
    number+=2


