from crease_finder.vertex import Vertex, Angle, Edge
import copy
from pprint import pprint
import itertools

def phantom_fold(vertex_map):
	return phantom_fold_inner(vertex_map[0], vertex_map)

def find_duplicate_constraint(constraints, this):
	for c in constraints:
		all_equal = True
		for key in c:
			if c[key] != this.get(key):
				all_equal = False
		if all_equal:
			return True

	return False



def phantom_fold_inner(vertex, vertex_map, constraints={}, checked=[]):
	# First check if we are constrianed
	out = []

	checked = copy.deepcopy(checked)
	checked.append(vertex.name)

	for fold in vertex.folds:
		# First verifify we follow constraint
		constraints_copy = copy.deepcopy(constraints)

		case_failed = False

		for edge, crease in zip(vertex.edges, fold):
			if edge.edge == None:
				continue

			# If we already constrained this edge to a different crease, we give up
			if edge.edge.name in constraints_copy:
				if constraints_copy[edge.edge.name] != crease:
					case_failed = True
					break

			if edge.edge.name not in constraints_copy:
				constraints_copy[edge.edge.name] = crease

		if case_failed:
			continue

		# Then pick another guy to phantom fold
		def is_not_complete(vertex):
			if vertex.name not in checked:
				return True
			for edge in vertex.edges:
				if not edge.edge:
					continue
				if edge.edge.name not in constraints_copy:
					return True
			return False

		incomplete_verticies = list(filter(is_not_complete, vertex_map))

		if len(incomplete_verticies) == 0:
			# Theres no more options in this path
			if find_duplicate_constraint(out, constraints_copy):
				continue

			out += [constraints_copy]
			continue

		for c in phantom_fold_inner(incomplete_verticies[0], vertex_map, constraints_copy, checked):
			if find_duplicate_constraint(out, c):
				continue
			out += [c]


	return out

#def main():
#	a = Vertex("a")
#	b = Vertex("b")
#	c = Vertex("c")
#	d = Vertex("d")
#
#	ab = Edge("ab", a, b)
#	ac = Edge("ac", a, c)
#
#	bc = Edge("bc", b, c)
#	bd = Edge("bd", b, d)
#
#	cd = Edge("cd", c, d)
#	da = Edge("da", d, a)
#
#	a.set_edges([Angle(40, ab), Angle(40, ac), Angle(140, da), Angle(140)])
#	b.set_edges([Angle(100, ab), Angle(60, bc), Angle(80), Angle(120)])
#	c.set_edges([Angle(40, bc), Angle(40, ac), Angle(140, cd), Angle(140)])
#	d.set_edges([Angle(100, bd), Angle(100, cd), Angle(80), Angle(80)])
#
#	pprint(phantom_fold_inner(a, [a, b, c, d], {}))

def main():
	a = Vertex("a")
	b = Vertex("b")
	c = Vertex("c")

	ab = Edge("ab", a, b)
	ac = Edge("ac", a, c)
	bc = Edge("bc", b, c)

	a.set_edges([Angle(60, ab), Angle(90), Angle(120), Angle(90, ac)])
	b.set_edges([Angle(60, bc), Angle(90), Angle(120), Angle(90, ab)])
	c.set_edges([Angle(60, ac), Angle(90), Angle(120), Angle(90, bc)])

	pprint(phantom_fold_inner(a, [a, b, c]))

if __name__ == '__main__':
	main()
