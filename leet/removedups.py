from sll import SinglyLinkedList


l = SinglyLinkedList()

lst = [1,5,2,6,3,2,1,1,5,3]

for i in lst:
	l.addTail(i)

def removeDup(sll):
	""" remove duplicates from a singly linked list """
	if sll.head is None: # empty linked list
		return

	walk = sll.head
	store = set()
	store.add(walk.data)

	while walk.next != None:
		if walk.next.data not in store:
			store.add(walk.next.data)
			walk = walk.next
		else:
			walk.next = walk.next.next

	print(store)
	p = sll.head
	while p != None:
		print(p.data)
		p = p.next

	return sll


def removeDup(sll):
	""" remove duplicates without use of a buffer """

	if sll.head is None: # empty linked list
		return
	mark = sll.head

	while mark != None:
		check = mark.next
		before = mark
		while check != None:
			if check.data == mark.data:
				before.next = check.next
				check.next = None
				check = before.next # advance the checker
			else:
				before = check
				check = check.next # advance the checker
		mark = mark.next

	p = sll.head
	while p != None:
		print(p.data)
		p = p.next

	return sll


def removeDup(sll):
	""" remove duplicates without use of a buffer, follow up """

	if sll.head is None: # empty linked list
		return
	mark = sll.head

	while mark != None:
		check = mark
		while check.next != None:
			if check.next.data == mark.data:
				check.next = check.next.next
			else:
				check = check.next # advance the checker
		mark = mark.next

	p = sll.head
	while p != None:
		print(p.data)
		p = p.next

	return sll

removeDup(l)