# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        pre = None
        cnt = 1
        p = head
        while cnt < m:
            pre = p
            p = p.next
            cnt += 1
        fr = ed = p
        while cnt < n:
            q = ed.next
            tmp = q.next
            if not pre is None:
                pre.next = q
            q.next = fr
            ed.next = tmp
            fr = q
            cnt += 1
        if pre != None:
            return head
        else:
            return fr