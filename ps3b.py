# Problem Set 3 (Part 2)
# Write the function subStringMatchExact. This function takes two arguments:
# a target string, and a key string. It should return a tuple of the starting
# points of matches of the key string in the target string, when indexing
# starts at 0. Complete the definition for
# def subStringMatchExact(target,key):

from string import *

def subStringMatchExact(target, key):
    """Returns all the starting points of matches of key in the target"""
    indices = ()
    index = find(target, key)
    if index == -1:
        print 'No matches found'
    else:
        indices = indices + (index, ) # add first match to tuple
        counter = 0 # counter to get existing value in tuple
        while len(target) >= len(key):
            # print 'while called with', target
            target = target[index + len(key):] # 1st match already found-> trim
            index = find(target, key)
            if index == -1:
                break
            else:
                newelement = indices[counter] + index + len(key) # new element
                # needs to account for the trimming. it will be:
                # existing index + current index + len(key)
                indices = indices + (newelement, )
                counter += 1 # new entry added to tuple
    return indices


