from vertex import Vertex, Angle, Edge
import copy
from pprint import pprint
import itertools

def phantom_fold(vertex, vertex_map, constraints):
	# First check if we are constrianed
	constraint = constraints.get(vertex.name, [None, None, None, None])

	out = []

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

		case_failed = False
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

				# This vertex is already constrained, if its different we have a failed case
				if constraints_copy[vert.name][i]:
					if constraints_copy[vert.name][i] != crease:
						case_failed = True

				constraints_copy[vert.name][i] = crease

		if case_failed:
			continue

		# Then pick another guy to phantom fold
		incomplete_verticies = list(filter(lambda n: constraints_copy.get(n.name) == None or None in constraints_copy.get(n.name), vertex_map))

		if len(incomplete_verticies) == 0:
			# Theres no more options in this path
			out += [constraints_copy]
			continue

		out += [*phantom_fold(incomplete_verticies[0], vertex_map, constraints_copy)]

	return out

#def main():
#	a = Vertex("a")
#	b = Vertex("b")
#	c = Vertex("c")
#	d = Vertex("d")
#
#	ab = Edge(a, b)
#	ac = Edge(a, c)
#
#	bc = Edge(b, c)
#	bd = Edge(b, d)
#
#	cd = Edge(c, d)
#	da = Edge(d, a)
#
#	a.set_edges([Angle(40, ab), Angle(40, ac), Angle(140, da), Angle(140)])
#	b.set_edges([Angle(100, ab), Angle(60, bc), Angle(80), Angle(120)])
#	c.set_edges([Angle(40, bc), Angle(40, ac), Angle(140, cd), Angle(140)])
#	d.set_edges([Angle(100, bd), Angle(100, cd), Angle(80), Angle(80)])
#
#	pprint(phantom_fold(a, [a, b, c, d], {}))

def main():
	a = Vertex("a")
	b = Vertex("b")
	c = Vertex("c")

	ab = Edge(a, b)
	ac = Edge(a, c)
	bc = Edge(b, c)

	a.set_edges([Angle(60, ab), Angle(90, ac), Angle(120), Angle(90)])
	b.set_edges([Angle(60, ab), Angle(90, bc), Angle(120), Angle(90)])
	c.set_edges([Angle(90), Angle(60, ac), Angle(90, bc), Angle(120)])

	pprint(phantom_fold(a, [a, b, c], {}))

if __name__ == '__main__':
	main()
