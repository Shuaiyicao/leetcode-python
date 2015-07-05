# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def __init__(self):
        self.found = False
    
    def dfs(self, node, sum):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return node.val == sum
        return self.dfs(node.left, sum - node.val) or self.dfs(node.right, sum - node.val)
        
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum)
        #return self.found