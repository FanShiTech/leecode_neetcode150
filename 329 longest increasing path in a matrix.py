"""

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #check each position , if its neighbor position is greater than that value, put a n , if there is no neighhbot posistion that's greaterr than that value , put 1


        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {} # (row, col)

        def dfs(r,c, preValue):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= preValue:
                return 0

            if(r,c) in dp:
                return dp[(r,c)]


            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            dp[(r,c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values())


    #o(m*n)