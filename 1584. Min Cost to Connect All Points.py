"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacent list  edges , aand then prime
        #o ( n^2 log n) n^2 represents number of edges , log n is prime


        # set() , minHeap, BFS, prim's algorithm.
        # find the distance between one point and each other point,
        #pop() the point that has the mininum weage , and repeat the same procedure


        N = len(points)

        adj = {i: [] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minH = [[0,0]] # [ cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue

            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res