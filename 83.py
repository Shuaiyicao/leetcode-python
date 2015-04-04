# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        p = head
        while p != None and p.next != None:
            while p.next != None and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head