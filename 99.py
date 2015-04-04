# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def __init__(self):
        self.trouble = []
        
    def dfs(self, node):
        if node is None:
            return (None, None)
            
        l_head, l_tail = self.dfs(node.left)
        if l_tail != None and node.val < l_tail.val:
            self.trouble.append(l_tail)
            self.trouble.append(node)
            
        r_head, r_tail = self.dfs(node.right)
        if r_head != None and node.val > r_head.val:
            self.trouble.append(node)
            self.trouble.append(r_head)
        
        l = l_head if l_head != None else node
        r = r_tail if r_tail != None else node
        return (l, r)
        
    def recoverTree(self, root):
        self.dfs(root)
        if len(self.trouble) == 2:
            tmp = self.trouble[0].val
            self.trouble[0].val = self.trouble[1].val
            self.trouble[1].val = tmp
        if len(self.trouble) == 4:
            if self.trouble[0].val < self.trouble[2].val and self.trouble[1].val < self.trouble[3].val:
                x = 1; y = 2
            else:
                x = 0; y = 3
            tmp = self.trouble[x].val
            self.trouble[x].val = self.trouble[y].val
            self.trouble[y].val = tmp
        return root