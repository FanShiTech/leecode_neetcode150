"""

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key=lambda P: P[0]**2 + P[1]**2)
        # return points[:k]

        # use min heap, compute distance, put into heapq[]

        minheap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minheap.append([dist, x, y])

        heapq.heapify(minheap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1

        return res
