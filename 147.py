class ListNode:
	def __init__(self, key):
		self.key = key
		self.next = None
		self.pre = None

class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		self._capacity = capacity
		self._tail = None
		self._head = None
		self._map = {}
		self._kv = {}
		self._used = 0

	def delete(self, node):
		if self._used == 1:
			self._head = self._tail = None
			return

		if node == self._head:
			if node.next != None:
				node.next.pre = None
			self._head = node.next
		elif node == self._tail:
			if node.pre != None:
				node.pre.next = None
			self._tail = node.pre
		else:
			node.pre.next = node.next
			node.next.pre = node.pre
	def insert(self, node):
		if self._tail != None:
			self._tail.next = node
			node.pre = self._tail
			self._tail = node
		else:
			self._tail = node
			self._head = node

	# @return an integer
	def get(self, key):
		if key not in self._map:
			return -1
		self.delete(self._map[key])
		tmp = ListNode(key)
		self.insert(tmp)
		self._map[key] = tmp
		return self._kv[key]

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		if key in self._map:
			self.delete(self._map[key])
			tmp = ListNode(key)
			self.insert(tmp)
			self._map[key] = tmp
			self._kv[key] = value
		else:
			if self._used == self._capacity:
				old_key = self._head.key
				self.delete(self._head)
				del self._kv[old_key]
				del self._map[old_key]
				self._used -= 1

			node = ListNode(key)
			self.insert(node)
			self._kv[key] = value
			self._map[key] = node
			self._used += 1

