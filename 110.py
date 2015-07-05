# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def dfs(self, node):
        if node is None:
            return (True, 0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left[1] > right[1]:
            left, right = right, left
        bal = left[0] and right[0] and right[1] - left[1] <= 1
        return (bal, right[1] + 1)
        
    def isBalanced(self, root):
        return self.dfs(root)[0]
