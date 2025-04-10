from vertex import Vertex, Angle

def vertex_tests():
	vertex = Vertex(
		"test",
		edges=[Angle(25), Angle(75), Angle(155), Angle(105)]
	)

	vertex = Vertex(
		"test",
		edges=[Angle(112.5), Angle(45), Angle(112.5), Angle(90)]
	)

	# Should have 8 ways
	vertex = Vertex(
		"test",
		edges=list(map(lambda x: Angle(x), [20, 70, 105, 30, 55, 80]))
	)

	vertex = Vertex(
		"test",
		edges=list(map(lambda x: Angle(x), [30, 30, 70, 40, 80, 110]))
	)

	# Should have 24 ways
	vertex = Vertex(
		"test",
		edges=list(map(lambda x: Angle(x), [20, 20, 40, 60, 60, 40, 60, 60]))
	)

	vertex = Vertex(
		"test",
		edges=list(map(lambda x: Angle(x), [40, 10, 20, 60, 60, 60, 60, 50]))
	)

	vertex = Vertex(
		"test",
		edges=list(map(lambda x: Angle(x), [60, 60, 60, 50, 40, 10, 20, 60]))
	)

if __name__ == '__main__':
	vertex_tests()

