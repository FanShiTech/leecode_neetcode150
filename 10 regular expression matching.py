"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""

justin128
justin128
Feb 13, 2023 18:59

Details
Solution
Python3
Runtime
31 ms
Beats
99.21%
Memory
14.2 MB
Beats
23.18%
Click the distribution chart to view more details
Notes

Related Tags

0/5
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        """
        a a b
        c * a * b
        if they dont match, we dont wanna use * (next position), so move that pointer to next next position

        top-down memorization

        """

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]


            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False


            match =  i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j+1) < len(p) and p[j + 1] == "*" :
                cache[(i,j)] = (dfs(i, j+2) or (match and dfs(i+1, j)))
                return cache[(i,j)]

            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return  cache[(i,j)]
            cache[(i,j)] = False
            return False

        return dfs(0,0)