
class ticTacToe(object):
	''' docstrings for tic tac toe game '''
	def __init__(self):
		super(ticTacToe, self).__init__()
		self.player = 'X'
		self.board = [['{:^15}'.format('')] *3 for j in range(3)]

	def play(self):
		''' handle user input and game logic '''
		try:
			i = int(input('enter row position\n'))
			j = int(input('enter column position\n'))
		except Exception:
			print("Please use valid integers as input\n")

		self.mark(i, j)

	def mark(self, i, j):
		''' make a mark at position i, j '''		
		if not( 0 <= i <= 2 and 0 <= j <= 2):
			raise ValueError('Invalid board position\n')
		if self.board[i][j] != '{:^15}'.format(''):
			raise ValueError('Board position occupied\n')
		if self.winner() is not None:
			print('\n' + self.winner())
		self.board[i][j] = '{:^15}'.format(self.player)
		if self.player == 'X':
			self.player = 'O'
		else:
			self.player = 'X'

	def issa_win(self, mark):
		''' check win configurations '''
		board = self.board
		return ( 
			mark == board[0][0] == board[0][1] == board[0][2] or #row 0
			mark == board[1][0] == board[1][1] == board[1][2] or #row 1
			mark == board[2][0] == board[2][1] == board[2][2] or #row 2
			mark == board[0][0] == board[1][0] == board[2][0] or #column 0
			mark == board[0][1] == board[1][1] == board[2][1] or #column 1
			mark == board[0][2] == board[1][2] == board[2][2] or #column 2
			mark == board[0][0] == board[1][1] == board[2][2] or #diagonal
			mark == board[0][2] == board[1][1] == board[2][0]    #reverse diag
			)

	def winner(self):
		''' mark of a player or None to indicate a tie '''
		for mark in 'XO':
			if self.issa_win('{:^15}'.format(mark)):
				return mark + ' wins!'
		return None

	def __str__(self):
		''' string representation of a current board game '''
		rows = ['|'.join(self.board[r]) for r in range(3)]
		return '\n\n'.join(rows)

game = ticTacToe()

while True:
	print('\n'+game.__str__()+'\n')	
	game.play()