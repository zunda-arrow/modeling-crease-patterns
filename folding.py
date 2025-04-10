from __future__ import annotations

import math
import itertools
import typing as t
from dataclasses import dataclass
import itertools

if t.TYPE_CHECKING:
	from vertex import Vertex

@dataclass
class FoldTree:
	# The total number of edges for this vertex
	edge_count: int

	crease_index: int
	next_crease: Dict['M' | 'V', FoldTree | None]

	def all_options(self):
		total_options = []
	
		for option in self.next_crease.items():
			k, v = option

			if v != None:
				options_following = v.all_options()
			else:
				options_following = [[None] * self.edge_count]

			for following in options_following:
				following[self.crease_index] = k

			total_options += options_following

		return total_options

def find_adjacent(index, array):
	if len(array) < 2:
		return list(filter(lambda x: x != index, [1, 0]))[0]
	if len(array) < 1:
		return []
	if (index == 0):
		return [1, len(array) - 1]
	if (index == len(array) - 1):
		return [1, len(array) - 2]
	return [index - 1, index + 1]

def find_adjacent_with_same_value(index, creases):
	out = []

	if (len(creases) <= 2):
		return []

	looking_at = index + 1
	while looking_at != index:
		if looking_at == len(creases):
			looking_at = 0
		if creases[looking_at] == creases[index]:
			out += [looking_at]
		else:
			break
		looking_at+=1

	looking_at = index - 1
	while looking_at != index:
		if looking_at == -1:
			looking_at = len(creases) - 1
		if creases[looking_at] == creases[index]:
			out += [looking_at]
		else:
			break
		looking_at-=1

	out += [index]

	return out

def verify_kawasaki(creases):
	a = 0
	b = 0

	for aa, bb in itertools.batched(creases, n=2):
		a += aa
		b += bb

	assert a == b, "Kawasaki's Theorem is not satisfied"

# Basic find fold number algoritm
# Original indecies keeps track of where a crease was "from"
def build_fold_tree_from_numbers(creases, original_indecies, edge_count):
	# Clone the lists to make code easier to follow
	creases = [*creases]
	original_indecies = [*original_indecies]

	verify_kawasaki(creases)

	if len(creases) == 2:
		# The function considers both orientations of mountains and valleys
		return FoldTree(edge_count, original_indecies[0], {
				'M': FoldTree(edge_count, original_indecies[1], {'M': None}),
				'V': FoldTree(edge_count, original_indecies[1], {'V': None}),
			}
		)
	
	lowest_index = creases.index(sorted(creases)[0])

	crease_size = creases[lowest_index]

	same = find_adjacent_with_same_value(lowest_index, creases)
	same_amount = len(same)

	# First find the options
	if same_amount % 2 == 1:
		options = math.comb(same_amount + 1, math.floor((same_amount + 1) / 2))
		combinations = list(itertools.combinations(range(same_amount + 1), math.floor((same_amount + 1) / 2)))

	if same_amount % 2 == 0:
		options = math.comb(same_amount + 1, math.floor(same_amount / 2) + 1)
		combinations = list(itertools.combinations(range(same_amount + 1), math.floor((same_amount / 2) + 1)))

	my_index = original_indecies[lowest_index]
	parter_index = my_index - 1
	if (parter_index < 0):
		parter_index = original_indecies[-1]

	# Then we remove the used of verticies
	for i in same:
		creases[i] = None
		original_indecies[i] = None

	if same_amount % 2 == 1:
		# We lose an odd number of creases
		(left, _) = find_adjacent(same[0], creases)
		(_, right) = find_adjacent(same[-1], creases)
		creases[left] = creases[left] + creases[right] - crease_size
		creases[right] = None

		original_indecies[right] = None

	if same_amount % 2 == 0:
		# We lose an even number of creases, do nothing
		pass

	creases = list(filter(lambda x: x != None, creases))
	original_indecies = list(filter(lambda x: x != None, original_indecies))

	for combination in combinations:
		# We say everything in the combination is a mountain, everything else is a valley
		print(combination)
		pass

	if options == 2:
		return FoldTree(edge_count, my_index, {
				'M': FoldTree(edge_count, parter_index, {'V': build_fold_tree_from_numbers(creases, original_indecies, edge_count)}),
				'V': FoldTree(edge_count, parter_index, {'M': build_fold_tree_from_numbers(creases, original_indecies, edge_count)})
			}
		)

# Build the fold tree for only one set set of mountains and valleys
def build_fold_tree(vertex: Vertex):
	angles = vertex.get_angles()
	return build_fold_tree_from_numbers(angles, list(range(len(angles))), len(angles))

