"""

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #o(sum(nums))

        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t+nums[i])
                nextDp.add(t)
            dp = nextDp

        return True if target in dp else False