# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
            
        p = head
        t_head = None
        pre = None
        
        while p != None:
            if p.next == None:
                break
            q = p.next
            tmp = q.next
            q.next = p
            p.next = tmp
            if pre == None:
                pre = p
                t_head = q
            else:
                pre.next = q
                pre = p
            p = tmp
        return t_head