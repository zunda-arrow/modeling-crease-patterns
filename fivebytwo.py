# This is a crease pattern that is not globally flat fodlable but we still
# are able to find a mountain valley assignment prediction


from crease_finder import Vertex, Edge, Angle, phantom_fold

def main():
	ab = Edge("ab")
	bc = Edge("bc")
	cd = Edge("cd")

	a = Vertex("a", [Angle(90, ab), Angle(90), Angle(90), Angle(90)])
	b = Vertex("b", [Angle(90, bc), Angle(90), Angle(90, ab), Angle(90)])
	c = Vertex("c", [Angle(90, cd), Angle(90), Angle(90, bc), Angle(90)])
	d = Vertex("d", [Angle(90), Angle(90), Angle(90, cd), Angle(90)])


	for result in phantom_fold([a, b, c, d]):
		a = result["a"]
		b = result["b"]
		c = result["c"]
		d = result["d"]

		if a[0] != 'V' or a[1] != 'V' or a[2] != 'V' and a[3] != 'M':
			continue
		if b[0] != 'M' or b[1] != 'V' or b[2] != 'V' and b[3] != 'V':
			continue
		if c[0] != 'V' or c[1] != 'V' or c[2] != 'M' and c[3] != 'V':
			continue
		if d[0] != 'M' or d[1] != 'V' or d[2] != 'V' and d[3] != 'V':
			continue
	

		print(result)


if __name__ == '__main__':
	main()


