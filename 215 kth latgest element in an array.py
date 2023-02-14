"""

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5


"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k


        def quickSort(l,r):
            pivot, pointer = nums[r], l #pointer is the index number

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer] # switch pointer and curr element
                    pointer+=1
            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:
                return quickSort(l, pointer-1)
            elif pointer < k:
                return quickSort(pointer+1, r)
            else:
                return nums[pointer]

        return quickSort(0, len(nums)-1)