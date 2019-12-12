class Layer():
	wide = 0
	tall = 0

	def __init__(self, wide, tall):
		self.wide=wide
		self.tall=tall
		self._digits = []

	def __repr__(self):
		return str(self._digits)

	def __len__(self):
		return len(self._digits)

	def __getitem__(self, item):
		return self._digits[item]

	@property
	def is_full(self):
		layer_capacity = self.wide*self.tall
		return len(self._digits) == layer_capacity

	def insert(self, n):
		self._digits.append(n)

	def no_of_nums(self, num):
		no_of_num = 0
		for i in self._digits:
			if i == num:
				no_of_num = no_of_num+1
		return no_of_num

def makeLayers(width,height, input):
	layers = []

	current_layer = Layer(width, height)
	
	while input:
		if current_layer.is_full:
			layers.append(current_layer)
			current_layer = Layer(width, height)

		i = input.pop(0)
		current_layer.insert(i)

	layers.append(current_layer)

	return layers


def main():
	width = 25
	length = 6

	nums = []

	with open('day8.txt', 'r') as f:
		for line in f:
			for char in line:
				nums.append(int(char))

	layers = makeLayers(width, length, nums)

	fewest_zeros_in_layer = layers[0].no_of_nums(0)
	fewest_zero_layer = None
	for layer in layers:
		if layer.no_of_nums(0) < fewest_zeros_in_layer:
			fewest_zero_layer = layer
			fewest_zeros_in_layer = layer.no_of_nums(0)

	print("answer:", fewest_zero_layer.no_of_nums(1) * fewest_zero_layer.no_of_nums(2))

	#part 2
	final_layer = ['#' for i in range(width*length)]
	layer_indexes = range(width*length)
	
	while layers:
		layer = layers.pop(0)
		for i in layer_indexes:
			pixel = layer[i]
			if pixel == 1: # white
				final_layer[i] = '#'
			elif pixel == 0: # black
				final_layer[i] = ' '
			else:
				continue
		
			index_to_remove = layer_indexes.index(i)
			layer_indexes.pop(index_to_remove)

	counter = 0
	for i in final_layer:
		counter = counter + 1
		print(i),
		if counter == 25:
			print("")
			counter = 0

main()