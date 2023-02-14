"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N =len(grid)
        visited = set()

        directions =[[0,1],[0,-1], [1,0], [-1,0]]
        minH = [[grid[0][0], 0, 0]]
        visited.add((0,0))

        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if ( neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR , neiC) in visited):
                    continue

                visited.add((neiR, neiC))
                heapq.heappush( minH, [max(t,grid[neiR][neiC]) , neiR, neiC] )