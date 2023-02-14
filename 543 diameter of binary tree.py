"""

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tc o(n) sc(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest(node):
            if not node:  #base case
                return 0

            nonlocal diameter.

            left_p = longest(node.left) #recursively find the longest path in left and right
            right_p = longest(node.right)

            diameter = max(diameter, left_p+right_p) # if left + right is longer than the current diameter, update itt

            return max(left_p, right_p) + 1

        longest(root)
        return diameter
