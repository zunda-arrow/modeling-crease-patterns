from vertex import Vertex, Angle, Edge
import copy
from pprint import pprint

def phantom_fold(vertex, constraints):
	# First check if we are constrianed
	constraint = constraints.get(vertex.name, [None, None, None, None])
	
	for fold in vertex.folds:
		# First verifify we follow constraint
		found_mismatch = False
		for f, c in zip(fold, constraint):
			if c == None:
				continue
			if f != c:
				found_mismatch = True
				break

		if found_mismatch:
			continue

		constraints_copy = copy.deepcopy(constraints)

		for i, (edge, crease) in enumerate(zip(vertex.edges, fold)):
			if vertex.name not in constraints_copy:
				constraints_copy[vertex.name] = [None, None, None, None]
			constraints_copy[vertex.name][i] = crease

			if edge.edge == None:
				continue

			verticies = edge.edge.verticies()

			for vert in verticies:
				if vert.name not in constraints_copy:
					constraints_copy[vert.name] = [None, None, None, None]

				constraints_copy[vert.name][i] = crease

		# Then pick another guy to phantom fold
		print(constraints_copy)
		phantom_fold(constraints_copy)


def main():
	a = Vertex("a")
	b = Vertex("b")
	c = Vertex("c")
	d = Vertex("d")

	ab = Edge(a, b)
	ac = Edge(a, c)

	bc = Edge(b, c)
	bd = Edge(b, d)

	cd = Edge(c, d)
	da = Edge(d, a)

	a.set_edges([Angle(90, ab), Angle(90, ac), Angle(90), Angle(90)])
	return
	b.set_edges([Angle(90, ab), Angle(90, bd), Angle(90), Angle(90)])
	c.set_edges([Angle(90, ac), Angle(90, cd), Angle(90), Angle(90)])
	d.set_edges([Angle(90, bd), Angle(90, cd), Angle(90), Angle(90)])

	return

	phantom_fold(a, {})


if __name__ == '__main__':
	main()
