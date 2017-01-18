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
s = 'habke'
indexInA = list([]) # list to store the corresponding index in a
indexInS = list([])
for i in range(len(s)):
    for j in range(len(A)):
        if s[i] == A[j]:
            indexInA += [j,]
            indexInS += [i,]

print indexInA, indexInS

matchA = []
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
    print "indexinA is %d value is %s" % (k, indexInA[k])
    print "matchA is ", matchA
    if len(matchA) == 0:
        matchA += [indexInA[k],]
        answer += s[k]
        print "match set to ", matchA
    else:
        if matchA[-1] > indexInA[k]:
            matchA = list([])
            answer = ''
            matchA += [indexInA[k], ]
            answer += s[k]
        else:
            matchA += [indexInA[k],]
            answer += s[k]

print matchA

print "Longest substring in alphabetical order is: ", answer




