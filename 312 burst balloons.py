"""

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def dp(i, j):
            if j - i < 2:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = 0
            for k in range(i + 1, j):
                combo = nums[i] * nums[j] * nums[k]
                res =  max(res, dp(i, k) + dp(k, j) + combo)
            memo[(i,j)] = res
            return memo[(i,j)]

        return dp(0, n - 1)

        """

        ex:
index   0  1. 2. 3. 4. 5
        1  3, 1, 5, 8  1
           L.        R

        if i pop() 3 the last, --- nums[l-1] * nums[l] * nums[r+1] + dp[i+1][r] || +dp[l][i-1]

        o(n^3)

        """