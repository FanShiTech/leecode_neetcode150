"""

234. Palindrome Linked List


 2 helper functions: 1) use fast and slow to get the middle point
                        2) create a reversed linked list

 1,2,2,1

1, 2  and  2, 1  then reverse the second half

compare two halfs


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        firstEnd = self.end_of_first_half(head)
        secondHalfStart = self.reverse_linked(firstEnd.next)

        result = True
        firstPos = head
        secondPos = secondHalfStart

        while result and secondPos is not None:
            if firstPos.val != secondPos.val:
                return False
            firstPos = firstPos.next
            secondPos = secondPos.next

        firstEnd.next = self.reverse_linked(secondHalfStart)
        return result

    def reverse_linked(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
