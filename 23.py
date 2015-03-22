# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def merge(self, a, b):
        if a == None:
            return b
        if b == None:
            return a
        t_head = ListNode(-1)
        res = t_head
        while a != None and b != None:
            if a.val > b.val:
                t_head.next = b
                t_head = b
                b = b.next
            else:
                t_head.next = a
                t_head = a
                a = a.next
        while a != None:
            t_head.next = a
            t_head = a
            a = a.next
        while b != None:
            t_head.next = b
            t_head = b
            b = b.next
        return res.next
        
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        n = len(lists)
        x = self.mergeKLists(lists[:n/2])
        y = self.mergeKLists(lists[n/2:])
        return self.merge(x, y)