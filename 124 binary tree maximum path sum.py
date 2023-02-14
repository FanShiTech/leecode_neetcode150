"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath = float('-inf')

        def dfs(node):
            nonlocal maxpath
            if not node:
                return 0

            leftmax = max(dfs(node.left),0)
            rightmax = max(dfs(node.right), 0)
            maxpath = max(maxpath, leftmax+rightmax+node.val)

            return max( leftmax+node.val, rightmax+node.val)

        dfs(root)
        return maxpath