"""

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):  # numbe of rotations we will Do
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            r -= 1  # update , and do inner layer
            l += 1