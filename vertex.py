from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Angle:
	# Distance from the last angle, given in terms of 360
	degree: int
	# The vertex this edge touches or None if this is the end of the paper
	vertex: Vertex | None = None

@dataclass
class Vertex:
	edges: list[Angle]

	def __post_init__(self):
		angle = sum(map(lambda x: x.degree, self.edges))
		if (angle != 360):
			raise Exception(f"Angle sum does not equal 360. Found sum={angle}.")


if __name__ == '__main__':
	vertex = Vertex(
		edges=[Angle(180), Angle(180)]
	)

