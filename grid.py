from crease_finder import Vertex, Edge, Angle, phantom_fold
from pprint import pprint

a = Vertex('a')
b = Vertex('b')

ab = Edge('ab', a, b)

a.set_edges([Angle(90, ab), Angle(90), Angle(90), Angle(90)])
b.set_edges([Angle(90, ab), Angle(90), Angle(90), Angle(90)])

folds = phantom_fold([a, b])

assert len(folds) == 32

# 2 * 3^(3 + 1)
# We can either pick (3 choose 2) OR pick all the same. Which gives 2 options.
# Then we double the final result because there is two sets of mountains and valleys.
print("Yep, that's 32 ways")

