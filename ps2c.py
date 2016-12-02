# Problem Set 2 (Part 4)
# Assume that the variable packages is bound to a tuple of length 3, the values
# of which specify the sizes of the packages, ordered from smallest to largest.
# Write a program that uses exhaustive search to find the largest number (less
# than 200) of McNuggets that cannot be bought in exact quantity.

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (10,10,20)   # variable that contains package sizes

for n in range(1, 201):   # only search for solutions up to size 150
    for i in range(0, 50):
        for j in range(0, 50):
            for k in range(0, 50):
                if((i*packages[0] + j*packages[1] + k*packages[2]) == n):
                    bestSoFar = n - 1
print 'Given package sizes <x>, <y>, and <z>, the largest number of \
McNuggets that cannot be bought in exact quantity is: ', bestSoFar

