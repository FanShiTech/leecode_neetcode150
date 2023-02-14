"""

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
"""


class Solution:
    def reverse(self, x: int) -> int:

        """
        num = 4562
        rev_num = 0
        rev_num = rev_num *10 + num%10 = 2
        num = num/10 = 456
        rev_num = rev_num *10 + num%10 = 20 + 6 = 26
        num = num/10 = 45
        rev_num = rev_num *10 + num%10 = 260 + 5 = 265
        num = num/10 = 4
        rev_num = rev_num *10 + num%10 = 2650 + 4 = 2654
        num = num/10 = 0

        rev = 0

        while(x > 0):
            a = x % 10
            rev = rev * 10 + a
            n = x // 10

        return rev

        cant do it with negative number
        """

        """
        to check if the reverse number is overflowed
        once the reverse is done, the reverse number / 10 , then i will get two parts. if the firsr part == the maximun 32 bit except the last didgit, then check the second part, see if the last digit > 7 ( maximun 32-bits: 2147483647) if yes, return 0


        """

        MIN = -2147483648
        MAX = 2147483647

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or res == MAX // 10 and digit >= MAX % 10:
                return 0

            if res < MIN // 10 or res == MIN // 10 and digit <= MIN % 10:
                return 0

            res = res * 10 + digit
        return res