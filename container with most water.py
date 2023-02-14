"""

use two pointers
area = high * width
we wanna take the min height from the beginning and the last number in the list



"""


def maxArea(li):
    maxarea = 0
    left = 0
    right = len(li) - 1

    while left < right:
        width = max(maxarea, min(li[left], li[right]) * width)

        if li[left] <= li[right]:
            left += 1
        else:
            right -= 1
    return maxarea
