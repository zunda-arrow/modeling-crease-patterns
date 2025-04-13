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

	crease_indecies: list[int]
	next_crease: list[tuple['M' | 'V']]
	next: FoldTree

	def all_options(self):
		total_options = []

		if self.next:
			option_set = self.next.all_options()

			for option in self.next_crease:
				for choice in option_set:
					choice = [*choice]
					for crease, index in zip(option, self.crease_indecies):
						choice[index] = crease
					total_options.append(choice)

			return total_options
		else:
			for option in self.next_crease:
				o = [None] * self.edge_count
				for crease, index in zip(option, self.crease_indecies):
					o[index] = crease

				total_options.append(o)
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
	while True:
		if looking_at == len(creases):
			looking_at = 0
		if looking_at == index:
			break
		if creases[looking_at] == creases[index]:
			out += [looking_at]
		else:
			break
		looking_at+=1

	looking_at = index - 1
	while True:
		if looking_at == -1:
			looking_at = len(creases) - 1
		if looking_at == index:
			break
		if creases[looking_at] == creases[index]:
			out += [looking_at]
		else:
			break
		looking_at-=1

	out += [index]

	# dedup the list
	return list(set(out))

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

	if len(creases) == 0:
		return None

	if len(creases) == 2:
		return FoldTree(edge_count, [original_indecies[0], original_indecies[1]], [['M', 'M'], ['V', 'V']], None)

	lowest_index = creases.index(sorted(creases)[0])
	crease_size = creases[lowest_index]

	same = find_adjacent_with_same_value(lowest_index, creases)
	same_amount = len(same)
	mapped_same = list(map(lambda x: original_indecies[x], same))

	if len(creases) == 4 and same_amount == 2:
			# we have a birds foot, I know this is the minimum requirements due to kawasaki's theorem
		birds_foot_start = (4 - lowest_index) % 4
		two = (4 - lowest_index + 1) % 4
		three = (4 - lowest_index + 2) % 4
		four = (4 - lowest_index + 3) % 4

		birds_foot_options = [
			['M', 'M', 'V', 'M'],
			['M', 'V', 'M', 'M'],
			['V', 'M', 'M', 'M'],
			['V', 'V', 'M', 'V'],
			['V', 'M', 'V', 'V'],
			['M', 'V', 'V', 'V'],
		]

		real_options = []

		for option in birds_foot_options:
			real_options.append([option[birds_foot_start], option[two], option[three], option[four]])

		return FoldTree(edge_count, original_indecies, real_options, None)

	# The index of the crease before the repeating pattern
	start = lowest_index
	number_checked = 0
	reduced = False
	while start in same:
		start -= 1
		if start < 0:
			start = len(creases) - 1

		number_checked += 1
		if number_checked >= len(original_indecies):
			parter_index = None
			# We reduce same_amount by 1, because later there should only be 4 choices to pick from, not 5
			same_amount -= 1
			reduced = True
			break
	else:
		parter_index = original_indecies[start]

	creases_that_will_be_folded = []
	if parter_index != None:
		creases_that_will_be_folded = [parter_index, *mapped_same]
	else:
		creases_that_will_be_folded = mapped_same

	# Map the itertools combinations to the original indecies
	def map_comb(comb):
		out = []
		for x in comb:
			# index 0 is the crease before the repeated creases
			out.append(list(map(lambda y: creases_that_will_be_folded[y], x)))
		return out

	if same_amount % 2 == 1:
		if reduced:
			combinations = map_comb(itertools.combinations(range(same_amount + 1), math.floor((same_amount + 3) / 2)))
		else:
			combinations = map_comb(itertools.combinations(range(same_amount + 1), math.floor((same_amount + 1) / 2)))

	if same_amount % 2 == 0:
		if reduced:
			combinations = map_comb(itertools.combinations(range(same_amount + 1), math.floor((same_amount / 2) + 2)))
		else:
			combinations = map_comb(itertools.combinations(range(same_amount + 1), math.floor((same_amount / 2) + 1)))

	if same_amount % 2 == 1:
		# We lose an odd number of creases
		(left, _) = find_adjacent(same[0], creases)
		(_, right) = find_adjacent(same[-1], creases)

		# Investigate why this order matters
		if creases[left] <= creases[right]:
			creases[left] = creases[left] + creases[right] - crease_size
			creases[right] = None
			original_indecies[right] = None
		else:
			creases[right] = creases[left] + creases[right] - crease_size
			creases[left] = None
			original_indecies[left] = None

	if same_amount % 2 == 0:
		# We lose an even number of creases, do nothing
		pass

	# Then we remove the used of verticies
	for i in same:
		creases[i] = None
		original_indecies[i] = None

	remaining_creases = list(filter(lambda x: x != None, creases))
	remaining_original_indecies = list(filter(lambda x: x != None, original_indecies))

	# Then lets do the same on the remaining!
	next = build_fold_tree_from_numbers(remaining_creases, remaining_original_indecies, edge_count)

	out_options = []

	for combination in combinations:
		# We say everything in the combination is a mountain, everything else is a valley
		mountains = combination
		valleys = list(filter(lambda x: x not in combination, creases_that_will_be_folded))

		creases = []

		for crease in creases_that_will_be_folded:
			if crease in mountains:
				creases += ['M']
			elif crease in valleys:
				creases += ['V']
			else:
				raise Exception("Crease not in mountain or valleys")

		out_options += [creases]

	return FoldTree(edge_count, creases_that_will_be_folded, out_options, next)

# Build the fold tree for only one set set of mountains and valleys
def find_all_folds(vertex: Vertex):
	angles = vertex.get_angles()
	tree = build_fold_tree_from_numbers(angles, list(range(len(angles))), len(angles))
	return tree.all_options()

