class GameBoard:
	
	def __init__(self, s):
			self.__space = ' '
			size = 3
			self.__board =  []
			
			for i in range (size):
				row = [' ']*size
				self.__board.append(row)

			
	def make_move(self, row, col, element):
		self.__board[row][col] = element
		
		
	def check_winner(self):
        # Given a board and a player's letter, this function returns True if  player has won.
		winner = (self.check_hz() or  self.check_vt() or
		(self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2] and self.__board[2][2] != self.__space) or
		(self.__board[0][2] == self.__board[1][1] and self.__board[1][1] == self.__board[2][0] and self.__board[2][0] != self.__space)) # check diagonal row top left to bottom right
		# when performing the check, and if there are three elements are equal, then make sure they are not equal to empty space ' ' which is what the 2D array was populated with at the start of the application.
		return winner	
		

	def check_hz(self): 
		row = ''
		for x in range(3):
			for y in range(3):
				row += self.__board[x][y]
            
			if 'XXX' in row or 'OOO' in row:
				return True
			row = ''
		return False  # return false if no winner was found

	def check_vt(self): 
		col = ''
		for y in range(3):
			for x in range(3):
				col += self.__board[x][y]
            
			if 'XXX' in col or 'OOO' in col:
				return True
			col = ''
		return False  # return false if no winner was found
		
	def is_board_full(self):
	    # TODO: Return True if every space on the board has been taken. Otherwise return False.
		row = ''
		for x in range(3):
			for y in range(3):
				row += self.__board[x][y]
            
			if ' ' in row :
				return False # found an empty cell, hence, the board is not full
			row = ''
		return True 
		
	def is_space_free (self, row, col):
		if self.__board[row][col] == " ":
			return True
		return False



	def show_board_dynamic(self):
		print()
		print('-------')
		for i in range (len(self.__board)):
			for j in range (len(self.__board)):
				print ("|", end = "")
				print (self.__board[i][j], end=""),
			print ("|")
			print('-------')
		print()
		