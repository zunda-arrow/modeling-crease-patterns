from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint

a = Vertex("a")
b = Vertex("b")
c = Vertex("c")

ab = Edge("ab", a, b)
ac = Edge("ac", a, c)
bc = Edge("bc", b, c)

a.set_edges([Angle(60, ab), Angle(90), Angle(120), Angle(90, ac)])
b.set_edges([Angle(60, bc), Angle(90), Angle(120), Angle(90, ab)])
c.set_edges([Angle(60, ac), Angle(90), Angle(120), Angle(90, bc)])

pprint(phantom_fold([a, b, c]))

print("There are no ways to fold this flat")

