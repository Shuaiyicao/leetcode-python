# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def compare(self, p, q):
        if p == None and q == None:
            return True
        if (p == None) or (q == None):
            return False
        if p.val != q.val:
            return False
        return self.compare(p.left, q.left) and self.compare(p.right, q.right)
        
    def isSameTree(self, p, q):
        return self.compare(p, q)