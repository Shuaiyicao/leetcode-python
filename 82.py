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
        first = now = None
        while p != None:
            if p.next != None and p.val == p.next.val:
                while p.next != None and p.val == p.next.val:
                    p = p.next
                p = p.next
            else:
               
                if first == None:
                    first = now = p
                else:
                    now.next = p
                    now = p
                p = p.next
        if now != None:
            now.next = None
        return first