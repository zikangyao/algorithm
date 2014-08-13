""" 
	N x N maze game
	find a path between upper left and bottom right
"""
from pprint import pprint
class MazeGame(object):
	def __init__(self, matrix):
		self.matrix = matrix
		self.N = len(matrix)
		self.sol_matrix = self._get_original_maze()

	def sol_maze(self, i, j):
		"""
		solve maze
		Args:
			i (int): the row of the next move
			j (int): the col of the next move
		"""
		if i == self.N-1 and j == self.N-1 \
			and matrix[self.N-1][self.N-1] == 1:
			self.sol_matrix[i][j] = 1
			return True

		if self._is_safe(i, j):
			# set sol matrix
			self.sol_matrix[i][j] = 1

			# try the bottom
			if self.sol_maze(i+1, j):
				return True

			# try the right
			if self.sol_maze(i, j+1):
				return True

			return False

		else:
			return False

	def _is_safe(self, i, j):
		"""
		check whether the point [i, j] is safe

		Args:
			matrix (list): 2 dimension list
			i (int): the row of the next move
			j (int): the col of the next move
		"""
		if i >= 0 and i <= self.N-1 and \
			j >= 0 and j <= self.N-1 and self.matrix[i][j] == 1:
			return True
		return False

	def _get_original_maze(self):
		"""
		get orignal maze (with all 0 in it)

		"""
		return [[0 for x in xrange(self.N)] for x in xrange(self.N)]


if __name__ == '__main__':
	matrix = [
		[1,0,0,1,0],
		[1,1,0,0,0],
		[0,1,1,0,0],
		[0,0,1,0,0],
		[0,0,1,1,1]
	]

	m = MazeGame(matrix)
	m.sol_maze(0,0)
	pprint(m.sol_matrix)