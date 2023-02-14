"""
118. Pascal's Triangle


"""


def pascalTriange(num):
    res = []

    for i in range(num):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]

        res.append(row)

    return res


num = 5

print(pascalTriange(5))
