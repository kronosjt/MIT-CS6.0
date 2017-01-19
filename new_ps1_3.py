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

s = 'abcdakakaka'
ans = s[0] # Initialize ans
tempans = ''

for i in range(1, len(s)):
        if ans[-1] <= s[i]: # check last element of ans vs next element of s
            ans += s[i] # add element of s to ans if it is bigger
        else:
            if len(ans) >= len(s[i:]):
                break # ans is longer than remaining elements in s so quit
            else:
                if len(tempans) < len(ans):
                    tempans = ans # update tempans only if it is shorter than ans
                    ans = ''
                    ans += s[i]
                else: # otherwise clear ans and continue
                    ans = ''
                    ans += s[i]

if len(tempans) >= len(ans):
    ans = tempans

print ("Longest substring in alphabetical order is: ", ans)




