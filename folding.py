import math
import itertools

from vertex import Vertex

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
def build_fold_tree_from_numbers(creases):
	verify_kawasaki(creases)

	if len(creases) == 2:
		return 2
	
	lowest_index = creases.index(sorted(creases)[0])

	crease_size = creases[lowest_index]

	same = find_adjacent_with_same_value(lowest_index, creases)
	same_amount = len(same)

	# First find the options
	if same_amount % 2 == 1:
		options = math.comb(same_amount + 1, math.floor((same_amount + 1) / 2))

	if same_amount % 2 == 0:
		options = math.comb(same_amount + 1, math.floor(same_amount / 2) + 1)

	# Then we remove the used of verticies
	for i in same:
		creases[i] = None

	if same_amount % 2 == 1:
		# We lose an odd number of creases
		(left, _) = find_adjacent(same[0], creases)
		(_, right) = find_adjacent(same[-1], creases)
		creases[left] = creases[left] + creases[right] - crease_size
		creases[right] = None

	if same_amount % 2 == 0:
		# We lose an even number of creases, do nothing
		pass

	creases = list(filter(lambda x: x != None, creases))

	return options * build_fold_tree(creases)

def build_fold_tree(vertex: Vertex):
	angles = vertex.get_angles()
	return build_fold_tree_from_numbers(angles)

