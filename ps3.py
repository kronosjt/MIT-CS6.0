# Problem Set 3
##Write two functions, called countSubStringMatch and countSubStringMatchRecursive
##that take two arguments, a key string and a target string. These functions
##iteratively and recursively count the number of instances of the key in the
##target string.

from string import *

### Iterative function 1
##
##def countSubStringMatch(target, key):
##    """Returns the number of instances of the key in the target string"""
##    count = 0
##    while( len(target) > 0):
##        if(int(find(target, key) == -1)):
##            print 'no match found'
##            break
##        else:
##            count += 1
##            target = target[(find(target, key))+len(key):] # remove (trim) key from target
##    print 'Number of matches found: ', count


# Iterative function 2

def countSubStringMatch(target, key):
    """Returns the number of instances of the key in the target string"""
    count = 0
    while (len(target) >= len(key)) and (find(target, key) != -1):
        count += 1
        target = target[(find(target, key))+len(key):] # remove (trim) key from target
    print 'Number of matches found: ', count

### Recursive function
##def countSubStringMatchRecursive(target, key):
##    """Recursive func that returns the number of matches"""
##    # print 'function called with', target
##    if (int(find(target, key) != -1)): # Base case
##        print 'Match found: '
##        countSubStringMatchRecursive(target[(find(target, key))+len(key):], key)
    
### Recursive function that returns only the number of matches
##def countSubStringMatchRecursive(target, key):
##    """Recursive func that returns the number of matches"""
##    print 'function called with', target
##    index = find(target,key)
##    if index == -1:
##        return 0
##    else:
##        return 1 + countSubStringMatchRecursive(target[index + len(key):],key)

        

    
    


