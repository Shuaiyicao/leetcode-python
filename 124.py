# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.ans = -1000000000
        
    def dfs(self, node):
        if node is None:
            return 0
            
        ret = node.val
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.ans = max(self.ans, ret)
        self.ans = max(self.ans, ret + left)
        self.ans = max(self.ans, ret + right)
        self.ans = max(self.ans, ret + left + right)
        
        ret = max(ret, node.val + left)
        ret = max(ret, node.val + right)
        
        return ret
        
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.dfs(root)
        return self.ans
        
