# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = now = None
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                if head == None:
                    head = now = l1
                else:
                    now.next = l1
                    now = l1
                l1 = l1.next
            else:
                if head == None:
                    head = now = l2
                else:
                    now.next = l2
                    now = l2
                l2 = l2.next
        while l1 != None:
            now.next = l1
            now = l1
            l1 = l1.next
        while l2 != None:
            now.next = l2
            now = l2
            l2 = l2.next
        if now != None:
            now.next = None
        return head