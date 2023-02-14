"""
392. Is Subsequence

use two points

while both pointers are smaller than len() of each string

compare them
if both positions' values are the same
both position += 1
else:
t += 1
return the s == len(s)
"""

def isSubsequence(s, t):
    l,r = 0,0

    while l < len(s) and r < len(t):
        if s[l] == t[r]:
            l+=1
            r+=1
        else:
            r+=1
    return l == len(s)


s = "abc"
t = "ahgd"

print(isSubsequence(s,t))