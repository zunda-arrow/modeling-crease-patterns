from vertex import Vertex, Angle

def vertex_tests():
	# Bird's foot
	vertex = Vertex(
		"test",
		edges=[Angle(60), Angle(60), Angle(120), Angle(120)]
	)
	print(vertex.folds)
	return

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
	print(len(vertex.folds))

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

