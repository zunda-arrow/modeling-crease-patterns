# Usage: python latticepy <width> <height>

from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint
import sys

# This file solves the stamp folding problem
def fold_lattice(n, m):
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

			# Bottom Edge
			if i < n:
				angles.append(Angle(90, vertical_edges[i][j]))
			else:
				angles.append(Angle(90))

			# Right Edge
			if j < n:
				angles.append(Angle(90, horizontal_edges[i][j]))
			else:
				angles.append(Angle(90))
			
			# Top Edge
			if i > 0:
				angles.append(Angle(90, vertical_edges[i - 1][j]))
			else:
				angles.append(Angle(90))

			# Right Edge
			if j > 0:
				angles.append(Angle(90, horizontal_edges[i][j - 1]))
			else:
				angles.append(Angle(90))

			verticies.append(Vertex(f"{i},{j}", angles))

	return verticies

def main():
	if len(sys.argv) < 3:
		print("Usage: `python lattice.py <width> <height>`")

	m = int(sys.argv[1])
	n = int(sys.argv[2])

	if m < 1:
		print("Minimum width is 2")
	if n < 1:
		print("Minimum height is 2")

	# We subtract one because we do not want to take the outside verticies into account
	folds = phantom_fold(fold_lattice(m - 1,n - 1))
	print("Found", len(folds), "ways")
	print("Actual:", 2 ** (m * n - 1))

if __name__ == '__main__':
	main()
