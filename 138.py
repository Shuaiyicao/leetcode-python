# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        
        q = head
        pre = None
        while not q is None:
            p = RandomListNode(q.label)
            tmp = q.next
            q.next = p
            if not pre is None:
                pre.next = q
            pre = p
            q = tmp
        
        q = head
        while not q is None:
            #tmp = q.next
            if not q.random is None:
                q.next.random = q.random.next
            if not q.next is None:
                q = q.next.next
            else:
                q = None
        
        q = head
        res = q.next
        while not q is None:
            tmp = q.next
            q.next = q.next.next
            if not tmp.next is None:
                tmp.next = tmp.next.next
            q = q.next
            
        return res
            
        
