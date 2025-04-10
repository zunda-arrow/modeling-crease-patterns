from __future__ import annotations

from dataclasses import dataclass
from folding import find_all_folds
from pprint import pprint
import itertools

def _verify_kawasaki(creases):
	a = 0
	b = 0

	for aa, bb in itertools.batched(creases, n=2):
		a += aa
		b += bb

	assert a == b, "Kawasaki's Theorem is not satisfied"

@dataclass
class Angle:
	# Distance from the last angle, given in terms of 360
	degree: int
	# The vertex this edge touches or None if this is the end of the paper
	vertex: Vertex | None = None

	# This program only looks for one solution set. We can flip the page to find the other solution set, so I am ignoring that
	# to make this easier to program.
	fold_type: 'mountain' | 'valley' | 'unknown' = 'unknown'

@dataclass
class Vertex:
	edges: list[Angle]

	def __post_init__(self):
		angle = sum(self.get_angles())
		_verify_kawasaki(self.get_angles())
		if (angle != 360):
			raise Exception(f"Angle sum does not equal 360. Found sum={angle}.")


	def get_angles(self):
		return list(map(lambda x: x.degree, self.edges))

if __name__ == '__main__':
	vertex = Vertex(
		edges=[Angle(25), Angle(75), Angle(155), Angle(105)]
	)

	# Should have 8 ways
	vertex = Vertex(
		edges=list(map(lambda x: Angle(x), [20, 70, 105, 30, 55, 80]))
	)

	# Should have 12 ways
	vertex = Vertex(
		edges=list(map(lambda x: Angle(x), [30, 30, 70, 40, 80, 110]))
	)

	# Should have 24 ways
	#vertex = Vertex(
	#	edges=list(map(lambda x: Angle(x), [20, 20, 40, 60, 60, 40, 60, 60]))
	#)

	#vertex = Vertex(
	#	edges=list(map(lambda x: Angle(x), [40, 10, 20, 60, 60, 60, 60, 50]))
	#)
	#vertex = Vertex(
	#	edges=list(map(lambda x: Angle(x), [60, 60, 60, 50, 40, 10, 20, 60]))
	#)

	folds = find_all_folds(vertex)
	pprint(folds)
	print(len(folds))

