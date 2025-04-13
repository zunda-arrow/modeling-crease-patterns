from vertex import Vertex, Angle

def verify(vertex, numbers: int | None = None):
	options = vertex.folds
	if numbers is not None:
		assert len(options) == numbers
	for option in options:
		print(vertex.name, option)
		assert None not in option

def vertex_tests():
	vertex = Vertex(
		"test 1",
		edges=[Angle(60), Angle(90), Angle(120), Angle(90)]
	)
	verify(vertex)

	# Bird's foot
	vertex = Vertex(
		"test 2",
		edges=[Angle(60), Angle(60), Angle(120), Angle(120)]
	)
	verify(vertex, 6)

	# rotated bird's foot
	vertex = Vertex(
		"test 3",
		edges=[Angle(120), Angle(60), Angle(60), Angle(120)]
	)
	verify(vertex, 6)

	# Should have 8 ways
	vertex = Vertex(
		"test 4",
		edges=list(map(lambda x: Angle(x), [20, 70, 105, 30, 55, 80]))
	)
	verify(vertex, 8)

	vertex = Vertex(
		"test 5",
		edges=list(map(lambda x: Angle(x), [30, 30, 70, 40, 80, 110]))
	)
	verify(vertex)

	# Should have 24 ways
	vertex = Vertex(
		"test 6",
		edges=list(map(lambda x: Angle(x), [20, 20, 40, 60, 60, 40, 60, 60]))
	)
	verify(vertex, 24)

	vertex = Vertex(
		"test 7",
		edges=list(map(lambda x: Angle(x), [40, 10, 20, 60, 60, 60, 60, 50]))
	)
	print(len(vertex.folds))

	vertex = Vertex(
		"test 8",
		edges=list(map(lambda x: Angle(x), [60, 60, 60, 50, 40, 10, 20, 60]))
	)
	print(len(vertex.folds))

if __name__ == '__main__':
	vertex_tests()

