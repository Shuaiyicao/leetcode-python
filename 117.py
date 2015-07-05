# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def dfs(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        
        tmp = node.next
        got = None
        while not tmp is None:
            if not tmp.left is None:
                got = tmp.left
                break
            elif not tmp.right is None:
                got = tmp.right
                break
            tmp = tmp.next
            
        if not node.left is None:
            if not node.right is None:
                node.left.next = node.right
                node.right.next = got
            else:
                node.left.next = got
        else:
            node.right.next = got
            
        
        self.dfs(node.right)
        self.dfs(node.left)
                    
    def connect(self, root):
        self.dfs(root)
