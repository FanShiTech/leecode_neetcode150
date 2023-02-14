"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.


"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0


        prevEnd = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prevEnd:
                prevEnd = e # not overlaped , update the prevEnd
            else:
                res += 1
                prevEnd = min(e, prevEnd)# only keep the min value of the end

        return res