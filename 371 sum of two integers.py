"""

Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
"""

"""

use & . ex: 0 & 0 = 0,    0 & 1 = 0 ,    1 & 1 = 1
use ^   ex:  0 ^ 0 = 0,    1 ^ 1 = 0,     1 ^ 0 = 1

a = 9 , b = 11
          1 0 0 1 --- 9
          1 0 1 1 --- 11
   
a^b        0 0 1 0
(a&b)<<1   first & 1 0 0 1, then << 1. 
  
  after first round
           0 0 1 0
         1 0 0 1 0
  second round
           1 0 0 0 0
         0 0 0 1 0 0
   thrid round
         0 1 0 1 0 0
         after ^ , we found there is no carry , whhich means the process ended
         010100 = 20 done      
    
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:

        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign
