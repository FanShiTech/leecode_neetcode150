"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findBound(nums, t, leftB):
            l,r = 0, len(nums)-1
            i = -1


            while l <= r:
                mid = (l+r) // 2

                if t > nums[mid]:
                    l = mid+1
                elif t < nums[mid]:
                    r = mid -1
                else:
                    i = mid
                    if leftB:
                        r = mid -1
                    else:
                        l = mid+1
            return i

        left = findBound(nums, target, True)
        right = findBound(nums, target, False)

        return [left, right]
