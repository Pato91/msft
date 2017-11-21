import unittest
import copy
from positionlist import PositionList

def insertionsort(lst):
	"""
	Insertion sort algorith for a positional list (lst)
	returns a sorted positional list
	"""
	if len(lst) > 1:
		marker = lst.first()
		while marker != lst.last():
			pivot = lst.after(marker)
			value = pivot.element()
			if value > marker.element():
				marker = pivot
			else:
				walk = marker
				while walk != lst.first() and lst.before(walk).element() > value:
					walk = lst.before(walk)
				lst.delete(pivot)
				lst.add_before(walk, value)
	return lst


class TestSortPL(unittest.TestCase):
	pl = PositionList()
	first = pl.add_first(22)
	second = pl.add_after(first, 11)
	third = pl.add_after(second, 99)
	fourth = pl.add_after(third, 88)
	fifth = pl.add_after(fourth, 9)
	sixth = pl.add_after(fifth, 7)
	seventh = pl.add_after(sixth, 42)
	def test_unsorted_pl(self):
		pl = self.pl
		self.assertEqual(len(pl), 7)
		self.assertEqual(list(iter(pl)), [22, 11, 99, 88, 9, 7, 42])

	def test_sort_pl(self):
		lst = copy.deepcopy(self.pl)
		lst_sorted = insertionsort(lst)
		self.assertEqual(list(iter(lst_sorted)), [7, 9, 11, 22, 42, 88, 99])

	def test_already_sorted(self):
		lst = copy.deepcopy(self.pl)
		lst_sorted = insertionsort(lst)
		self.assertEqual(list(iter(lst_sorted)), list(iter(insertionsort(lst_sorted))))

if __name__ == '__main__':
	unittest.main()