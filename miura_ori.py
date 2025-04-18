# Usage: python miura_ori.py <width> <height>
# Known bug: Miura Ori of size 2,4 gives 108 combinations but it should be 54

from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint
import sys

# This file solves the stamp folding problem
def fold_ori(n, m):
	# First we set the edges
	max_n = max(n, m)

	horizontal_edges = []
	vertical_edges = []

	for i in range(max_n):
		vertical_edges.append([])
		for j in range(max_n):
			vertical_edges[-1].append(Edge(f"{j},{i} to {j},{i + 1}"))

	for j in range(max_n):
		horizontal_edges.append([])
		for i in range(max_n):
			horizontal_edges[-1].append(Edge(f"{j},{i} to {j + 1},{i}"))

	verticies = []

	for i in range(n):		
		for j in range(m):
			angles = []

			if i % 2 == 0:
				# Bottom Edge
				if i < n:
					angles.append(Angle(120, vertical_edges[i][j]))
				else:
					angles.append(Angle(120))

				# Right Edge
				if j < n:
					angles.append(Angle(60, horizontal_edges[i][j]))
				else:
					angles.append(Angle(60))
				
				# Top Edge
				if i > 0:
					angles.append(Angle(60, vertical_edges[i - 1][j]))
				else:
					angles.append(Angle(60))

				# Left Edge
				if j > 0:
					angles.append(Angle(120, horizontal_edges[i][j - 1]))
				else:
					angles.append(Angle(120))
			else:
				# Right Edge
				if j < n:
					angles.append(Angle(120, horizontal_edges[i][j]))
				else:
					angles.append(Angle(120))
				
				# Top Edge
				if i > 0:
					angles.append(Angle(120, vertical_edges[i - 1][j]))
				else:
					angles.append(Angle(120))

				# Left Edge
				if j > 0:
					angles.append(Angle(60, horizontal_edges[i][j - 1]))
				else:
					angles.append(Angle(60))

				# Bottom Edge
				if i < n:
					angles.append(Angle(60, vertical_edges[i][j]))
				else:
					angles.append(Angle(60))

			verticies.append(Vertex(f"{i},{j}", angles))
	
	return verticies

# From https://oeis.org/A078099
KNOWN_MIURA_VALUES = [
1, 2, 2, 4, 6, 4, 8, 18, 18, 8, 16, 54, 82, 54, 16, 32, 162, 374, 374, 162, 32, 64, 486, 1706, 2604, 1706, 486, 64, 128, 1458, 7782, 18150, 18150, 7782, 1458, 128, 256, 4374, 35498, 126534, 193662, 126534, 35498, 4374, 256, 512, 13122, 161926, 882180, 2068146, 2068146, 882180, 161926, 13122, 51211111
]

def triangle_number(n):
	if n == 0:
		return 0
	return n + triangle_number(n - 1)

def main():
	if len(sys.argv) < 3:
		print("Usage: `python miura_ori.py <width> <height>`")
		return

	m = int(sys.argv[1])
	n = int(sys.argv[2])

	if m < 2:
		print("Minimum width is 2")
		return
	if n < 2:
		print("Minimum height is 2")
		return

	# We subtract one because we do not want to take the outside verticies into account
	folds = phantom_fold(fold_ori(m - 1,n - 1))
	print("Found", len(folds), "ways")
	print("Actual:", KNOWN_MIURA_VALUES[triangle_number(m + n - 1) - n])

if __name__ == '__main__':
	main()
