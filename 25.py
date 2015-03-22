# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse_k(self, head, k):
        
        p = head
        for i in range(k - 1):
            p = p.next
            if p == None: return (head, None, None)
                
        p = head
        t_head = head
        for i in range(k - 1):
            if p.next != None:
                q = p.next
                tmp = q.next
                q.next = t_head
                t_head = q
                p.next = tmp
            
        return (t_head, p, p.next)
        #return (t_head, None, None)
                
                
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        if head is None:
            return None
        
        p = head
        res = None
        pre = None
        while p != None:
            t_head, t_tail, tail = self.reverse_k(p, k)
            if res == None:
                res = t_head
                pre = t_tail
            else:
                pre.next = t_head
                pre = t_tail
            p = tail
        return res