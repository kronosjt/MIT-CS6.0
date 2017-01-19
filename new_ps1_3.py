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

s = 'abcbcd'
answer = s[0]

for i in range(1, len(s)):
    if len(answer) < len(s[i:]):
        if answer[-1] > s[i]:
            answer = ''
            answer += s[i]
        else:
            answer += s[i]
    elif len(answer) == len(s[i:]):
        if answer[-1] < s[i]:
            answer += s[i]
    else:
        break
print "Longest substring in alphabetical order is: ", answer




