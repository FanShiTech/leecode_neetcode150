"""

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        # capture unsurrounded region
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (
                        r in [0, ROWS - 1] or c in [0, COLS - 1]):  # check if regions are connected to border

                    capture(r, c)

        # capture surrounded region
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture unsurrouunded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
