"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # min heap and hashmap

        #n (log n * n)

        if len(hand) % groupSize != 0:
            return False

        count = {}

        for n in hand:
            count[n] =  1+count.get(n, 0) # if there is no n in the hashmap, ceate one and the count should be 1

        minH = list( count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if i != minH[0]:
                        return False

                    heapq.heappop(minH)  # pop the value if count[i].value is 0

        return True