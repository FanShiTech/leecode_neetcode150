"""
54 Spiral Matrix

"""


def spiralMatrix(matrix):
    row = len(matrix)

    if row == 0 or len(matrix[0]) == 0:
        return []

    col = len(matrix[0])

    res = matrix[0]  # res [1,2,3,4]

    if row > 1:
        for i in range(1, row):
            res.append(matrix[i][col - 1])

        for j in range(col - 2, -1, -1):
            res.append(matrix[row - 1][j])

        if col > 1:
            for i in range(row - 2, 0, -1):
                res.append(matrix[i][0])

    M = []
    for k in range(1, row - 1):
        t = matrix[k][1:-1]
        M.append(t)

    return res + spiralMatrix(M)


num = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralMatrix(num))

"""
        res = []
        left, right = 0, len(matrix[0])  # right is the number of columns,here right is 3
        top, bottom = 0 , len(matrix)  #bottom is the number of the rows, here bottom is 3

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -=1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


"""