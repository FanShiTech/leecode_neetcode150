"""

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # can not be visited twice , no loop
        # o (e + v)

        if not n:
            return True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)  # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True