class Layer():
	wide = 0
	tall = 0
	limit = 0
	digits = []

	def __init__(self, wide, tall):
		self.wide=wide
		self.tall=tall
		self.limit = wide*tall
		self.digits = []

	def __repr__(self):
		return str(self.digits)

	def __len__(self):
		return len(self.digits)

	@property
	def is_full(self):
		layer_capacity = self.wide*self.tall
		if len(self.digits) > layer_capacity:
			raise Exception("layer capacity breached")
		return len(self.digits) == layer_capacity

	def insert(self, n):
		self.digits.append(n)

	def no_of_nums(self, num):
		no_of_num = 0
		for i in self.digits:
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
	# create layer
	# add 6 rows to layer
	# add 25 pixels to the row.
	# when all rows and layers are done create a new layer

	# get layer containing fewest 0s
	# how many 1s in that layer * no of 2s in that layer
	nums = [1,1,1,3,4,5,6,7,8,1,0,1,2]
	nums = []

	with open('day8.txt', 'r') as f:
		for line in f:
			for char in line:
				nums.append(int(char))

	layers = makeLayers(25,6, nums)

	fewest_zeros_in_layer = layers[0].no_of_nums(0)
	fewest_zero_layer = None
	for layer in layers:
		if layer.no_of_nums(0) < fewest_zeros_in_layer:
			fewest_zero_layer = layer
			fewest_zeros_in_layer = layer.no_of_nums(0)

	print("no of layers", len(layers))
	print(layer.no_of_nums(0))
	print(layer.no_of_nums(1))
	print(layer.no_of_nums(2))
	print("answer:", fewest_zero_layer.no_of_nums(1) * fewest_zero_layer.no_of_nums(2))




main()