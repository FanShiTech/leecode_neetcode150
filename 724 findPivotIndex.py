
"""
724. Find Pivot Index

"""

def pivotIndex(li):
    S = sum(li)
    leftsum = 0

    for index, value in enumerate(li):
        if leftsum == (S - leftsum - value):  # ex: 28 - 0 - 1
            return index
        leftsum += value     # ex: if no match, leftsum = 1
    return -1


# TC = O(N)
# SC = O(1)

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))

"""
use the sum of the list - leftsum - current value . 
if they are match, reutrn the current value index
otherwise leftsum increase 

"""

