import numpy as np

bd = np.zeros((9,9), dtype=np.int16)

# Thank you to stackoverflow user Nagasaki45 for the code to display the board
# (Pretty tasteless username though, bud)

def display(bd):
	print('')
	for i, row in enumerate(bd):
		if i in [3,6]:
			print('|-------+-------+-------|')
		print('| ', end='')
		for j, cell in enumerate(row):
			if j in [3,6]:
				print('| ', end='')
			print(cell, end=' ')
			if j is 8:
				print('|', end='')
		print('')

display(bd)

