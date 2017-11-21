import unittest
from positionlist import PositionList

class FavoritesList:
	"""
	List of elements ordered from the most frequently accessed to the least accessed
	Is a positional list
	"""
	class _Item:
		"""
		Non-public nested Item class
		Stores the element of a list and its access count as a single instance
		( composition pattern - OOP DESIGN PATTERN )
		"""
		__slots__ = '_value', '_count' # streamline memory
		def __init__(self, e):
			""" Initialize an item """
			self._value = e
			self._count = 0

	# Non-public utility methods -------------------------

	def _find_position(self, e):
		""" Search for element e and return its Position, None if not found """
		walk = self._data.first()
		while walk is not None and walk.element()._value != e:
			walk = self._data.after(walk)
		return walk

	def _move_up(self, p):
		""" Move an item at position p earlier in the list based on access count """
		if p != self._data.first():
			count = p.element()._count
			walk = self._data.before(p)
			if count > walk.element()._count:
				while walk != self._data.first() and count > self._data.before(walk).element()._count:
					walk = self._data.before(walk)
				self._data.add_before(walk, self._data.delete(p)) # delete and reinsert element


	# Public accessor and mutator methods ---------------

	def __init__(self):
		""" Create an empty list of favorites """
		self._data = PositionList()

	def __len__(self):
		""" Return number of entries in favorites list """
		return len(self._data)

	def is_empty(self):
		""" Return True if list is empty """
		return len(self._data) == 0

	def add(self, e):
		"""
		Add an element to the list and return its position
		New Items have zero counts and are added to the back of list
		"""
		return self._data.add_last(self._Item(e))

	def access(self, e):
		"""
		Access element e and return its former position
		Elements access count increases and it moves towards the top as a favorite
		"""
		p = self._find_position(e)
		if p is None: # if element doesnt exist, add one
			p = self._data.add_last(self._Item(e))
		p.element()._count += 1
		self._move_up(p)

	def remove(self, e):
		"""Remove element e from the list of favorites """
		p = self._find_position(e)
		if p is not None:  # delete if found in list
			p._data.delete(p)

	def top(self, k):
		""" Generate sequence of top k elements  in the favorites list """
		if not 1 <= k <= len(self): # top 100 out of five? ha!
			raise ValueError('Illegal value for k')
		walk = self._data.first()
		for i in range(k):
			item = walk.element()
			yield item._value
			walk = self._data.after(walk)


class TestFavoritesList(unittest.TestCase):

	def test_fav_list_empty_when_created(self):
		fl = FavoritesList()
		self.assertTrue(fl.is_empty())
		self.assertEqual(len(fl), 0)

	def test_add_item_to_list(self):
		fl = FavoritesList()
		first = fl.add("First")
		second = fl.add("Second")
		self.assertEqual(first.element()._count, 0)
		self.assertEqual(second.element()._count, 0)

	def test_access_element(self):
		""" accessing element should increase its count """
		fl = FavoritesList()
		pass

	def test_remove_element(self):
		fl = FavoritesList()
		pass

	def test_top_favs(self):
		""" test accessing list of k most favorites """
		fl = FavoritesList()
		pass


if __name__ == '__main__':
	unittest.main()
