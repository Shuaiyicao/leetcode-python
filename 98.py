# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def check(self, node, lower_bound, upper_bound):
        if node is None:
            return True
        if node.val <= lower_bound or node.val >= upper_bound:
            return False
        return self.check(node.left, lower_bound, node.val) and self.check(node.right, node.val, upper_bound)
        
    def isValidBST(self, root):
        return self.check(root, -1<<30, 1<<30)