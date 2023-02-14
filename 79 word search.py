"""

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true


"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        path = set()# to make sure we dont revisit the past

        def dfs(r,c, i): # i is curr chara
            if i == len(word): #means we have reached the laast position
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path ):
                return False

            path.add( (r,c))

            res = ( dfs(r+1, c, i+1) or  # i+1 means we found the character we needed, and move to the next
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1) )

            path.remove((r,c))