"""

54 spiral matrix
space: O(m*n)
memory: 0(1)

"""


def spiralOrder(li):
    res = []

    left, right = 0, len(li[0])  # right is the number of columns
    top, bottom = 0, len(li)  # bottom is the number of rows

    while left < right and top < bottom:
        for i in range(left, right):
            res.append(li[top][i])  # append 1,2,3
        top += 1  # the first row is done, top increase 1, top moves to the second row

        for i in range(top, bottom):
            res.append(li[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            res.append(li[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            res.append(li[i][left])
        left += 1

    return res


li = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(spiralOrder(li))