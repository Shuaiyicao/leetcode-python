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
        self.res = 0
    
    def dfs(self, node, now):
        now = now * 10 + node.val
        if node.left is None and node.right is None:
            self.res += now
        if node.left:
            self.dfs(node.left, now)
        if node.right:
            self.dfs(node.right, now)
            
    def sumNumbers(self, root):
        if root is None:
            return 0
        
        self.dfs(root, 0)
        return self.res