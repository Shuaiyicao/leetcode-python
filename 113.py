# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def dfs(self, node, sum):
        if node is None:
            return []
        if node.left is None and node.right is None:
            if node.val == sum:
                return [ [node.val] ]
            else:
                return []
        left = self.dfs(node.left, sum - node.val)
        right = self.dfs(node.right, sum - node.val)
        res = []
        for item in left:
            if len(item) == 0:
                continue
            item.insert(0, node.val)
            res.append(item)
        for item in right:
            if len(item) == 0:
                continue
            item.insert(0, node.val)
            res.append(item)

        return res
        
    def pathSum(self, root, sum):
        return self.dfs(root, sum)
