# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
        small_head = big_head = None
        small_now = big_now = None
        while head != None:
            if head.val < x:
                if small_head == None:
                    small_head = small_now = head
                else:
                    small_now.next = head
                    small_now = head
            else:
                if big_head == None:
                    big_head = big_now = head
                else:
                    big_now.next = head
                    big_now = head
            head = head.next
        
        if big_now != None:
            big_now.next = None
            
        if small_head == None:
            return big_head
        else:
            small_now.next = big_head
            return small_head