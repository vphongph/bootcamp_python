import numpy as np

class NumPyCreator:
	def from_list(self, lst, dtype=None):
		return np.array(lst, dtype)

	def from_tuple(self, tup, dtype=None):
		return np.array(tup, dtype)

	def from_iterable(self, it, dtype=None):
		return np.array(it, dtype)

	def from_shape(self, shape, value=0, dtype=None):
		return np.full(shape, value, dtype)

	def identity(self, shape, dtype=None):
		return np.identity(shape, dtype)

	def random(self, shape):
		return np.random.rand(shape[0],shape[1])



npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))

print(npc.from_tuple(("a", "b", "c")))

print(npc.from_iterable(range(5)))

shape=(3,5)
print(npc.from_shape(shape))

print(npc.random(shape))

print(npc.identity(4))