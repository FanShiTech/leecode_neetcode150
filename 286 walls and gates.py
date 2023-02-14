"""

ou are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # starts from both gates, use BFS
        # TC SC: O(M*N)

        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or rooms[r][
                c] == -1):  # means the row is out of boundaries.
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:  # for entire matrix, if the position is 0,
                    q.append([r, c])  # add to queue
                    visited.add((r, c))  # and add to visited, so we wont visited it again

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                rooms[r][c] = dist  # change the gate possition to dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1