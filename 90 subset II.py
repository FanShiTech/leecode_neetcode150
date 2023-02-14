"""

Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]


        nums.sort()

        def backtrack(index, cur_subset):
            #base case
            if index == len(nums):
                res.append(cur_subset.copy())
                return

            # two decisions to make , 1- include nums[i]
            cur_subset.append(nums[index])
            backtrack(index+1, cur_subset) #move index to the next position
            cur_subset.pop() # the step that prepares for the 2 decision


            # 2- do not include nums[i]
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index+=1 # ex [ 1,2,2,3] , we only need one 2

            backtrack(index + 1, cur_subset)

        backtrack(0, [])
        return res