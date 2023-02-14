"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0, 0
        # rob1, rob2 , n , n+1  , .....
        #if you wannna robber n , you must robber robber 1
        # if you wanna robber n , you cant include rob2
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2 # move to next place
            rob2 = temp # move to the next place
        return rob2 # because rob2 will be arrived the last position