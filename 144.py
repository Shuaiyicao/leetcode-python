# Definition for singly-linked list.
#class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reverse(self, p):
		pre = p
		p = p.next
		while not p is None:
			tmp = p.next
			p.next = pre
			pre = p
			p = tmp
		return pre

	def reorderList(self, head):
		n = 0
		p = head
		while not p is None:
			n += 1
			p = p.next
		if n < 2:
			return 
		p = head
		for i in xrange((n - 1) / 2):
			p = p.next
		tmpp = p.next
		p.next = None
		x = head
		y = self.reverse(tmpp)
		tmpp.next = None
		while not y is None and not x is None:
			tmpx = x.next
			tmpy = y.next
			x.next = y
			y.next = tmpx
			x = tmpx
			y = tmpy
			
