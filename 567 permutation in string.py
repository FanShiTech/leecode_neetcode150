"""

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

"""

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1c, s2c = [0]*26, [0]*26
    for i in range(len(s1)):
        s1c[ord(s1[i]) - ord('a')] += 1
        s2c[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1c[i] == s2c[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        index =  ord(s2[r]) - ord('a')
        s2c[index] += 1
        if s1c[index] == s2c[index]:
            matches += 1
        elif s1c[index] + 1 == s2c[index]:
            matches-=1

