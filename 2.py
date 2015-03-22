# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        first = 0
        base = 1
        while l1 != None:
            first += l1.val * base
            l1 = l1.next
            base *= 10
        second = 0
        base = 1
        while l2 != None:
            second += l2.val * base
            l2 = l2.next
            base *= 10
        first += second
        
        if first == 0:
            return ListNode(0)
            
        pre = None
        tail = None
        while first != 0:
            tmp = ListNode(first % 10)
            first /= 10
            if pre == None:
                pre = tail = tmp
            else:
                tail.next = tmp
                tail = tmp
        return pre