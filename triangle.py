from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint

ab = Edge("ab")
ac = Edge("ac")
bc = Edge("bc")

a = Vertex("a", [Angle(60, ab), Angle(90), Angle(120), Angle(90, ac)])
b = Vertex("b", [Angle(60, bc), Angle(90), Angle(120), Angle(90, ab)])
c = Vertex("c", [Angle(60, ac), Angle(90), Angle(120), Angle(90, bc)])

pprint(phantom_fold([a, b, c]))

print("There are no ways to fold this flat")

