# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
            
        k = 0
        p = head
        q = head
        pre = None
        while k < n:
            p = p.next
            k += 1
        if p == None:
            return q.next
        while p != None:
            p = p.next
            pre = q
            q = q.next
        pre.next = q.next
        return head
