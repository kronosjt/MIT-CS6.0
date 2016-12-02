# Problem Set 2 (Part 3)
# Write an iterative program that finds the largest number of McNuggets that
# cannot be bought in exact quantity. Your program should print the answer
# in the following format
# Largest number of McNuggets that cannot be bought in exact quantity:

McNuggets = 1 # Start at 1 & go up to 49. We know 49 can be bought.
Answers = ()
while(McNuggets<50):
    isDivisible = False
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if((i*6 + j*9 + k*20) == McNuggets):
                    isDivisible = True
    if(isDivisible == False):
        Answers += (McNuggets,)                    
    McNuggets+=1
print 'Largest number of McNuggets that cannot be bought in exact quantity:', Answers[-1]
