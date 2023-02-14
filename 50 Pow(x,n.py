"""

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        # x^-n = 1 / x^n

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            # if n == 5, or odd number, x * x^2 * x^2  = x ^ 5
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
