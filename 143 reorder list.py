"""
You are given the head of a singly linked-list. The list can be represented as:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # break the linked list into half -half by using fast slow
        slow, fast = head, head.next

        while fast and fast.next:  # creating two lists
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # the begining of the second
        prev = slow.next = None
        # reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2