from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint

a = Vertex('a')
b = Vertex('b')

ab = Edge('ab', a, b)

a.set_edges([Angle(90, ab), Angle(90), Angle(90), Angle(90)])
b.set_edges([Angle(90, ab), Angle(90), Angle(90), Angle(90)])

folds = phantom_fold([a, b])

pprint(folds)

vertex = Vertex(
	"test 4",
	edges=list(map(lambda x: Angle(x), [20, 70, 105, 30, 55, 80]))
)

assert len(folds) == 32

print("Yep, that's 32 ways")


