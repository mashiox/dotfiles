'''
Determine whether a 9x9 sudoku board is valid

# Attempt 1
Every iteration of n, add 3.

n = 0
C = ["5", "6", ".", "8", "4", "7", ".", ".", "."]
R = ["5", "3", ".", ".", "7", ".", ".", ".", "."]
T = [
	["5", "3", "."],
	["6", ".", "."],
	[".", "9", "8"]
]

# Attempt 2
Every iteration of n, add 3

n = 0
R0 = ["5","3",".",".","7",".",".",".","."]
R1 = ["6",".",".","1","9","5",".",".","."]
R2 = [".","9","8",".",".",".",".","6","."]
T0 = [
	["5","3","."],
	["6",".","."],
	[".","9","8"],
]
T1 = [
	[".","7","."],
	["1","9","5"],
	[".",".","."],
]
T2 = [
	[".",".","."],
	[".",".","."],
	[".","6","."],
]

'''

import collections

def isValidSudoku(board):
	return isValidSudoku_etl(board) and isValidSudoku_hash(board)

def isValidSudoku_hash(board):
	# Dictionaries where the values are hash sets
	rows = collections.defaultdict(set)
	cols = collections.defaultdict(set)
	trip = collections.defaultdict(set)

	for r in range(9):
		for c in range(9):
			val = board[r][c]

			# Skip empty cells
			if val == ".": continue

			# Check for dupes
			if (val in rows[r] or
	   			val in cols[c] or
				val in trip[ ( r//3, c//3) ]
	   		): return False

			# add to collection for persistence
			rows[r].add(val)
			cols[c].add(val)
			trip[( r//3, c//3 )].add(val)

	return True

def isValidSudoku_etl(board):
	validBoard = True

	for n in range(0, 3):
		# Long Rows from the matrix
		R0 = board[ 3*n ]
		R1 = board[ 3*n + 1 ]
		R2 = board[ 3*n + 2 ]
		# Long Columns from the matrix
		C0 = [ row[ 3*n ] for row in board ]
		C1 = [ row[ 3*n + 1 ] for row in board ]
		C2 = [ row[ 3*n + 2 ] for row in board ]
		# Build 3x3 triples submatrix
		T0 = [
			R0[ 0:3 ],
			R1[ 0:3 ],
			R2[ 0:3 ],
		]
		T1 = [
			R0[ 3:6 ],
			R1[ 3:6 ],
			R2[ 3:6 ],
		]
		T2 = [
			R0[ 6:9 ],
			R1[ 6:9 ],
			R2[ 6:9 ],
		]
		# Build an object that tells us how many duplicates it ran into in a triple matrix
		F0 = {
			item: { "count": T0[ 0 ].count(item) + T0[ 1 ].count(item) + T0[ 2 ].count(item) }
			# Flatten each triple to a list
			for sublist in T0 for item in sublist if item != "."
		}
		F1 = {
			item: { "count": T1[ 0 ].count(item) + T1[ 1 ].count(item) + T1[ 2 ].count(item) }
			for sublist in T1 for item in sublist if item != "."
		}
		F2 = {
			item: { "count": T2[ 0 ].count(item) + T2[ 1 ].count(item) + T2[ 2 ].count(item) }
			for sublist in T2 for item in sublist if item != "."
		}
		# Find any repeated values in the triple
		Tres0 = { k: v for k, v in F0.items() if v['count'] > 1 }
		Tres1 = { k: v for k, v in F1.items() if v['count'] > 1 }
		Tres2 = { k: v for k, v in F2.items() if v['count'] > 1 }

		if Tres0:
			validBoard = False
		if Tres1:
			validBoard = False
		if Tres2:
			validBoard = False

		# Keep it Simple: Just recalculate the long vectors for validity
		G0 = {
			item: { "count": R0.count(item) }
			for sublist in R0 for item in sublist if item != "."
		}
		G1 = {
			item: { "count": R1.count(item) }
			for sublist in R1 for item in sublist if item != "."
		}
		G2 = {
			item: { "count": R2.count(item) }
			for sublist in R2 for item in sublist if item != "."
		}
		# Column Problem: We recalculate this every iteration of n
		H0 = {
			item: { "count": C0.count(item) }
			for sublist in C0 for item in sublist if item != "."
		}
		H1 = {
			item: { "count": C1.count(item) }
			for sublist in C1 for item in sublist if item != "."
		}
		H2 = {
			item: { "count": C2.count(item) }
			for sublist in C2 for item in sublist if item != "."
		}

		# Find any repeated values from the vectors
		Ures0 = { k: v for k, v in G0.items() if v['count'] > 1 }
		Ures1 = { k: v for k, v in G1.items() if v['count'] > 1 }
		Ures2 = { k: v for k, v in G2.items() if v['count'] > 1 }
		Vres0 = { k: v for k, v in H0.items() if v['count'] > 1 }
		Vres1 = { k: v for k, v in H1.items() if v['count'] > 1 }
		Vres2 = { k: v for k, v in H2.items() if v['count'] > 1 }

		if (Ures0 or Vres0):
			validBoard = False
		if (Ures1 or Vres1):
			validBoard = False
		if (Ures2 or Vres2):
			validBoard = False

	return validBoard
	# return True

print("Valid Board:")
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
if (isValidSudoku(board)):
	print("Correct: board valid")
else:
	print("Error: Board should have been valid")

print("Invalid Board:")

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
if (isValidSudoku(board)):
	print("Error: Board should have been INvalid")
else:
	print("Correct: board invalid")

print("Valid Board")
board = [
  [".",".",".",".","5",".","2",".","."],
  [".",".","6",".",".",".",".","3","."],
  [".","2",".","4",".",".",".",".","."],
  ["1",".",".",".",".","3",".",".","."],
  [".",".",".","7",".",".","6",".","."],
  [".",".",".",".","8",".",".",".","1"],
  [".","9",".",".",".",".",".",".","."],
  [".",".",".","6",".",".","4",".","."],
  ["3",".",".",".",".",".",".","8","."]
]
if (isValidSudoku(board)):
	print("Valid Board")