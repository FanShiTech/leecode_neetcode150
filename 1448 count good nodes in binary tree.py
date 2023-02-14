"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:


        def helper(node,maxval):
            if not node:
                return 0

            res = 1 if node.val >= maxval else 0
            maxval = max(maxval, node.val) # by doing this , we can pass maxval into recursion function
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)
            return  res

        return helper(root,, root.val)
