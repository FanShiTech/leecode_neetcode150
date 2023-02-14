"""

1480. Running Sum of 1d Array

assign p as an list which contains the first element of the list

in the range from second element of the list to its end
append the sum of the current element and the element of the p

"""


def runningSum(li):
    p = [li[0]]
    for i in range(1, len(li)):
        p.append(li[i] + p[i - 1])
    return p


nums = [1, 2, 3, 4]
print(runningSum(nums))

"""


"""