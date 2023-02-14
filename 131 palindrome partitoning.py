"""
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        part = []

        def dfs(cur_index):
            if cur_index >= len(s):  #base case
                res.append(part.copy())
                return

            for j in range(cur_index, len(s)):
                if self.isPali(s, cur_index, j):
                    part.append(s[cur_index: j+1])
                    dfs(j+1)
                    part.pop()



        dfs(0)
        return res

    def isPali(self, s,l,r):
        while l < r:
            if s[l] != s[r] :
                return False
            l, r = l+1, r-1

        return True