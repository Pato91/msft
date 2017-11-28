import sys
sys.path.append('D:\\LEARN\\code\\msft\\linkedlists')
from slinkedqueue import LinkedQueue


"""Merge-sort based on a linked data structure """

def merge(s1, s2, s):
	""" Merge two sorted queue instances s1, s2 into empty queue s """
	while not s1.is_empty() and not s2.is_empty():
		if s1.first() < s2.first():
			s.enqueue(s1.dequeue())
		else:
			s.enqueue(s2.enqueue())
	while not s1.is_empty(): # add remaining elements of s1 to s
		s.enqueue(s1.dequeue())
	while not s2.is_empty(): # add remaining elements of s2 to s
		s.enqueue(s2.enqueue())

def mergeSort(q):
	n = len(q)
	if n < 2:
		return q
	else:
		mid = n // 2
		s1 = LinkedQueue()
		s2 = LinkedQueue()
		_sorted = LinkedQueue()
		while len(s1) < mid:
			s1.enqueue(q.dequeue())
		while not q.is_empty():
			s2.enqueue(q.dequeue())
		mergeSort(s1)
		mergeSort(s2)

		merge(s1, s2, _sorted)

		return _sorted


q = LinkedQueue()
# add elements to queue

print(mergeSort(q))