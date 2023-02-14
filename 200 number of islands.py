"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):

            q = collections.deque()  # put everything into the q, visited
            visited.add((r, c))
            q.append((r, c))

            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc  # determine the next position
                    if (r in range(rows) and
                            c in range(cols) and
                            (r, c) not in visited and
                            grid[r][c] == " 1"):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        return count
