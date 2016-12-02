# Problem Set 3 (Part 3)
# Write a function, called which takes three arguments: a tuple
# representing starting points for the first substring, a tuple representing
# starting points for the second substring, and the length of the first
# substring. The function should return a tuple of all members (call
# it n) of the first tuple for which there is an element in the second tuple
# call it k) such that n+m+1 = k, where m is the length of the first substring.
# Complete the definition
# def constrainedMatchPair(firstMatch,secondMatch,length):

from string import *

def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allCorrectMatches = ()
    for miss in range (0, len(key)):
        key1 = key[:miss] 
        key2 = key[miss+1:]
        print 'converting key', key, 'into pairs', key1, ' & ', key2

        starts1 = subStringMatchExact(target, key1)
        starts2 = subStringMatchExact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(starts1, starts2, len(key1))
        allCorrectMatches = allCorrectMatches + filtered
        print 'starts 1=', starts1
        print 'starts 2=', starts2
        print 'all possible matches for', key1, key2, 'starts at', filtered
    return allCorrectMatches
                


def subStringMatchExact(maintarget, subkey):
    """Returns all the starting points of matches of key in the target"""
    indices = ()
    index = find(maintarget, subkey)
    if index == -1 or len(subkey) == 0:
        return ()
    else:
        indices = indices + (index, ) # add first match to tuple
        counter = 0 # counter to get existing value in tuple
        while len(maintarget) >= len(subkey):
            # print 'while called with', target
            maintarget = maintarget[index + len(subkey):] # 1st match already found-> trim
            index = find(maintarget, subkey)
            if index == -1:
                break
            else:
                newelement = indices[counter] + index + len(subkey) # new element
                # needs to account for the trimming. it will be:
                # existing index + current index + len(key)
                indices = indices + (newelement, )
                counter += 1 # new entry added to tuple
    return indices

def constrainedMatchPair(firstMatch, secondMatch, length):
    """returns tuple of all members of first tuple (n) for which there is an element/
    in the second tuple (k) such that n+m+1=k, where m=len(key1)"""
    answers = ()
    print 'len of matches_key1', len(firstMatch)
    print 'len of matches_key2', len(secondMatch)
    for n in range(0, len(firstMatch)):
        for k in range(0, len(secondMatch)):
            calculated_k = int(firstMatch[n]) + int(length) + 1
            print 'calculated_k=', calculated_k
            if calculated_k == secondMatch[k]:
                answers = answers + (firstMatch[n],)
    return answers
    
