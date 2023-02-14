"""

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

"""


class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        # We must multiply the number by -1 because
        # Python doesn't include built-in max-heap atm.
        heappush(self.first_half, -num)
        popped_element = heappop(self.first_half)
        heappush(self.second_half, -popped_element)

        if len(self.first_half) < len(self.second_half):
            popped_element = heappop(self.second_half)
            heappush(self.first_half, -popped_element)

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        return -self.first_half[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()