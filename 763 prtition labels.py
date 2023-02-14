"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, v in enumerate(s):
            lastIndex[v] = i  # store the last index of the element seen in the array

        res = []
        size = 0
        end = 0
        for i, v in enumerate(s):
            size += 1
            end = max(end, lastIndex[v])

            if i == end:
                res.append(size)

                size = 0

        return res
