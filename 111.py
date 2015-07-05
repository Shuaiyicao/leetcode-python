# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def dfs(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        res = 1<<30
        if node.left:
            res = min(res, self.dfs(node.left))
        if node.right:
            res = min(res, self.dfs(node.right))
        return res + 1
    def minDepth(self, root):
        return self.dfs(root)
