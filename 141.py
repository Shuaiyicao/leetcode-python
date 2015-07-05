# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def walk(self, node):
        if node is None:
            return None
        return node.next
        
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head
        circle = False
        while slow and fast:
            slow = self.walk(slow)
            fast = self.walk(fast)
            fast = self.walk(fast)
            if slow and fast and slow == fast:
                circle = True
                break
        return circle