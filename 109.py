# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def __init__(self):
        self.a = []
    def build(self, num):
        if len(num) == 0:
            return None
        n = len(num)
        root = TreeNode(num[n/2])
        root.left = self.build(num[:n/2])
        root.right = self.build(num[n/2+1:])
        return root
        
    def sortedListToBST(self, head):
        if head == None:
            return None
            
        while head != None:
            self.a.append(head.val)
            head = head.next
        n = len(self.a)
        return self.build(self.a)