"""
Problem 3
15.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

# PSEUDOCODE:
#   - For each letter in s we check the index in alphabets.
#   - index l should be greater than index (l-1) for them to be in alphabetical order

A = "abcdefghijklmnopqrstuvwxyz"
s = 'azcbobobegghakl'
indexInS = list([]) # list to store index of letter in s
indexInA = list([]) # list to store the corresponding index in a

for i in range(len(s)): # we need to find the index in a for each letter in s
    for j in range(len(A)):
        if s[i] == A[j]:
            indexInA += [j,]
            indexInS += [i,]

print indexInA, indexInS

letInOrder = [] # list to store indices for letters that are in order
answer = ''

# for k in range(0,len(indexInA)):
#     print "indexinA is %d value is %s" % (k, indexInA[k])
#     print "match is ", match
#     if len(match) == 0:
#         match += [indexInA[k],]
#         print "match set to ", match
#     else:
#         if k != len(indexInA)-1:
#             if match[-1] > indexInA[k]:
#                 match = list([])
#                 match += [indexInA[k], ]
#             else:
#                 match += [indexInA[k],]


for k in range(0,len(indexInA)-1):
    if len(letInOrder) >= len(indexInA[k:]):
        break
    print "indexinA is %d value is %s" % (k, indexInA[k])
    print "letInOrder is ", letInOrder
    if len(letInOrder) == 0: # Initialize matchA
        letInOrder += [indexInA[k],]
        answer += s[k]
        print "letInOrder set to ", letInOrder
    else:
        if letInOrder[-1] > indexInA[k]:
            letInOrder = list([])
            answer = ''
            letInOrder += [indexInA[k], ]
            answer += s[k]
        else:
            letInOrder += [indexInA[k],]
            answer += s[k]

print letInOrder

print "Longest substring in alphabetical order is: ", answer




