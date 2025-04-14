from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')

ab = Edge('ab', a, b)
ac = Edge('ac', a, c)
bd = Edge('bd', b, d)
cd = Edge('cd', c, d)

a.set_edges([Angle(90, ac), Angle(90, ab), Angle(90), Angle(90)])
b.set_edges([Angle(90, ab), Angle(90, bd), Angle(90), Angle(90)])
c.set_edges([Angle(90, cd), Angle(90, ac), Angle(90), Angle(90)])
d.set_edges([Angle(90, bd), Angle(90, cd), Angle(90), Angle(90)])

folds = phantom_fold([a, b, c, d])

assert len(folds) == 15

print("Yep, thats 15 ways")


