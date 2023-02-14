"""

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


"""


def topKF(li, k):
    count = {}
    freq = [[] for i in range(len(li) + 1)]

    for n in li:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)


    res = []

    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
