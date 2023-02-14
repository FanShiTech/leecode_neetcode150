"""
Easy
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

ex: l = [1,2,3,4]
    outcome = [1,3,6,10]
"""


def runningSum(nums):
    p = [nums[0]]  # defined the first element

    for i in range(1, len(nums)):  # go from the second element
        p.append(nums[i] + p[i - 1])  # append ( nums current number  + the last p number )
    return p

# TC : O(N)
# SC : O(1)