from vertex import Vertex, Angle


def main():
	a = Vertex()
	b = Vertex()
	c = Vertex()
	d = Vertex()

	a.set_edges([Angle(90, b), Angle(90, c), Angle(90), Angle(90)])
	b.set_edges([Angle(90, a), Angle(90, d), Angle(90), Angle(90)])
	c.set_edges([Angle(90, a), Angle(90, d), Angle(90), Angle(90)])
	d.set_edges([Angle(90, b), Angle(90, c), Angle(90), Angle(90)])


if __name__ == '__main__':
	main()
