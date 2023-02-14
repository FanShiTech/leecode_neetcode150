"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

"""
import collections
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res  = []
        q = collections.deque([root])

        while q :
            rightside = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node: # this node is the one node thats left, which is the right most
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)

        return res