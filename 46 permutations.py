"""

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        #base case

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)): #ex: [1,2,3]
            n = nums.pop(0) # n = 1
            perms = self.permute(nums) # all the way down to len(nums) == 1

            for perm in perms:
                perm.append(n) # ex: perms: 3, -> 3,2
            result.extend(perms)

            nums.append(n)
        return result