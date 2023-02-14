"""

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""

def findMin(nums):
    res = nums[0]
    l, r = 0 , len(nums)-1

    for l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        mid = (l+r)//2
        res  = nums[mid]
        if nums[mid] >= nums[l]:
            l = m+1
        else:
            r = m-1

    return res