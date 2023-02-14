"""

Given two strings s and t, return the number of distinct
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i,j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0 # there is no potential match case
            if( i, j) in cache:
                return cache[(i,j)]

            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                cache[(i,j)] = dfs(i+1, j)
            return cache[(i,j)]

        return dfs(0,0)