"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC=O(N). SC=O(N)
        if len(s) != len(t):
            return False

        sl, tl = {}, {}
        for i in range(len(s)):
            sl[s[i]] = 1 + sl.get(s[i], 0)
            tl[t[i]] = 1 + tl.get(t[i], 0)

        for j in sl:

            if sl[j] != tl.get(j, 0):
                return False

        return True


# create two dict, compare their values
#pay attention on hot to use get()