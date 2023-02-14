"""


Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        word1  = "", word2 = "" , do nothing
        word1 = abc , word2 = abc , do nothhing
        word1 = abc, word2 = "", delete word1
        wor1 = "" , word2 = "abc, insert word1

        word1 = abd, word2 = acd,
        if w1[i] == w2[j], i+1, j+1, else replace

        """


        cache = [ [float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1) ]
        for j in range(len(word2)+ 1):
            cache[len(word1)][j] = len(word2) - j  # bottom row
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i


        """
        [inf, inf, inf, 5], 
        [inf, inf, inf, 4], 
        [inf, inf, inf, 3], 
        [inf, inf, inf, 2], 
        [inf, inf, inf, 1], 
        [3, 2, 1, 0]]
> 


        """

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1]) # 3 operations


                """
                [3, 3, 4, 5], 
                [3, 2, 3, 4], 
                [2, 2, 2, 3], 
                [3, 2, 1, 2], 
                [3, 2, 1, 1], 
                [3, 2, 1, 0]]

                """

        return cache[0][0]