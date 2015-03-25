# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
            
        n = 0
        t_head = head
        while head != None:
            n += 1
            tail = head
            head = head.next
        k %= n
        if k == 0:
            return t_head
            
        head = t_head
        for i in range(n - k - 1):
            head = head.next
        
        new_head = head.next
        head.next = None
        tail.next = t_head
        return new_head