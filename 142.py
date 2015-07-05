# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def walk(self, node):
        if node is None:
            return None
        return node.next
    
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
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
        if circle == False:
            return None
        slow = head
        while slow != fast:
            slow = self.walk(slow)
            fast = self.walk(fast)
        return slow
