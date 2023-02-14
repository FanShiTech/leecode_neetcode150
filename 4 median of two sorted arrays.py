"""

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


"""

lass
Solution:


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    """
   B  1,2,3,4,5,6,7,8

    make sure a has less length

    A 1,2,3,4,5

    """

    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2  # for A
        j = half - i - 2  # pointer for B

        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

        if Aleft <= Bright and Bleft <= Aright:

            if total % 2 == 1:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bleft:
            r = i - 1
        else:
            l = i + 1

