"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DECISSION TREE -> CACHE
        """
        leetcode
            <-
        e= dp[7] not match with any string in wordDict, size is not match too
        d = dp[6] = dp[5] = false
        c = dp[4] = True because code == code




        """

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]