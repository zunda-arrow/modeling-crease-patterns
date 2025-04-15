from __future__ import annotations

from dataclasses import dataclass
from crease_finder.fold_vertex import find_all_folds
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
class Edge:
	name: str

@dataclass
class Angle:
	# Distance from the last angle, given in terms of 360
	degree: int
	# The edge this vertex is one, or none if it touches the edge of the paper
	edge: Edge | None = None

@dataclass
class Vertex:
	name: str
	edges: list[Angle]

	def __post_init__(self):
		angle = sum(self.get_angles())
		_verify_kawasaki(self.get_angles())
		if (angle != 360):
			raise Exception(f"Angle sum does not equal 360. Found sum={angle}.")
		self.folds = find_all_folds(self)

	def get_angles(self):
		return list(map(lambda x: x.degree, self.edges))

