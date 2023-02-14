"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # check each index . ex: 1,2,4,3.  index 0 =1  -> [1,2], [1,4], [1,3] -> since 4 & 3 > 2, so  [1,2,4], [1,2,3] -> [1,2,3]
        #                                   index 1 can only have 2 elements total; index 2 can have 1, index 3 can only have 1
        # o(N^2)


        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)