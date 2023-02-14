"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.



Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

"""



"""
Sort queries and intervals.
Iterate queries from small to big,
and find out all open intervals [l, r],
and we add them to a priority queue.
Also, we need to remove all closed interval from the queue.

In the priority, we use
[interval size, interval end] = [r-l+1, r] as the key.

The head of the queue is the smallest interval we want to return for each query.

"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)[::-1]

        heap = []
        res = {}

        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                i, j = intervals.pop()
                if j >= q:
                    heapq.heappush(heap, [j-i+1, j])
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]