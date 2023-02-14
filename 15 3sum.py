"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

tc: o( n log n ) + o(n ^ 2)  = o(n^2)
sc: o(n)
"""


def threeSum(n):
    res = []
    n.sort()

    for i, a in enumerate(n):
        if i > 0 and a == [i - 1]:
            continue

        l, r = i + 1, len(n) - 1
        while l < r:
            total = a + n[l] + n[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append([a, n[l], n[r]])
                l += 1
                while n[l] == n[l - 1] and l < r:
                    l += 1
    return res


nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))