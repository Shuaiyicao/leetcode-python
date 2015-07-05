# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def build(self, num):
        if len(num) == 0:
            return None
        n = len(num)
        root = TreeNode(num[n/2])
        root.left = self.build(num[:n/2])
        root.right = self.build(num[n/2+1:])
        return root
        
    def sortedArrayToBST(self, num):
        return self.build(num)
