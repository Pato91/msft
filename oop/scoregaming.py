import unittest


class GameEntry:
	def __init__(self, name='test', score=20):
		self.name = name
		self.score = score

	def getName(self):
		return self.name

	def getScore(self):
		return self.score

	def updateScore(self, score):
		self.score = score

	def __str__(self):
		''' string representation of an game entry '''
		return '[ {name}, {score} ]'.format(name = self.name, score = self.score)


class ScoreBoard:
	def __init__(self, capacity=5):
		self.capacity = capacity
		self.board  = [None]*capacity
		self.count = 0

	def getEntry(self, position):
		if position < 1:
			raise Exception('Wuut! not possible')
		elif position > self.capacity:
			return 'Not on Leaderboard'
		return self.board[position-1]

	def updateBoard(self, entry):
		score = entry.getScore()
		if self.count < self.capacity or score > self.board[-1].getScore():
			if self.count < self.capacity: # no score to drop from list
				self.count += 1
			# shifting lower scores rightward
			j = self.count - 1
			while j > 0 and self.board[j-1].getScore() < score:
				self.board[j] = self.buard[j-1]
				j -= 1
			self.board[j] = entry

	def __str__(self):
		''' string representation of leaderboard '''
		return '\n'.join( str(entry) for entry in self.board )


class TestsEntries(unittest.TestCase):
	def test_entry_template(self):
		self.assertTrue(GameEntry())

	def test_entry_has_name(self):
		entry = GameEntry()
		self.assertTrue(entry.name)

	def test_entry_has_score(self):
		entry = GameEntry()
		self.assertTrue(entry.score)

	def test_can_create_entry(self):
		entry = GameEntry('Goosipher 2.O', 666)
		self.assertEqual(entry.name, 'Goosipher 2.O')
		self.assertEqual(entry.score, 666)

	def test_score_access(self):
		entry = GameEntry('Goosipher 2.O', 666)
		self.assertEqual(entry.getName(), 'Goosipher 2.O')
		self.assertEqual(entry.getScore(), 666)

	def test_update_score(self):
		entry = GameEntry('Goosipher 2.O', 666)
		entry.updateScore(1000)
		self.assertEqual(entry.getScore(), 1000)

	def test_get_entry_repr(self):
		entry = GameEntry('Goosipher 2.O', 666)
		self.assertEqual(entry.__str__(), '[ Goosipher 2.O, 666 ]')


class TestBoard(unittest.TestCase):
	def test_create_board(self):
		self.assertTrue(ScoreBoard())

	def test_capacity(self):
		leaderboard = ScoreBoard(10)
		self.assertEqual(len(leaderboard.board), 10)

	def test_get_entry(self):
		leaderboard = ScoreBoard(10)
		self.assertEqual(leaderboard.getEntry(10), None)
		self.assertEqual(leaderboard.getEntry(11), 'Not on Leaderboard')

	def test_exceptions(self):
		leaderboard = ScoreBoard()
		with self.assertRaisesRegex(Exception, 'Wuut! not possible'):
			leaderboard.getEntry(0)

	def test_update_board(self):
		leaderboard = ScoreBoard()
		goos = GameEntry('Goosipher 2.O', 666)
		leaderboard.updateBoard(goos)

		self.assertEqual(leaderboard.getEntry(1).__str__(), '[ Goosipher 2.O, 666 ]')


	def test_board_representation(self):
		leaderboard = ScoreBoard()
		self.assertEqual(leaderboard.__str__(), 'None\nNone\nNone\nNone\nNone')


if __name__ == '__main__':
	unittest.main()
