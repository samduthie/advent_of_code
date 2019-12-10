# list of orbits
# H orbits G orbits B orbits COM
# C orbits B orbits COM

class Node(object):
	parent = None
	name = ''

	def __init__(self, name, parent=None):
		self.parent = parent
		self.name = name

	def __repr__(self):
		return self.name

	def no_of_parents(self):
		p = 0
		parent = self.parent
		while True:
			if parent:
				p = p + 1
				parent = parent.parent
			else: break
		return p

def get_node(nodes, name):
	for node in nodes:
		if node.name == name:
			return node

	return None

def main():
	nodes = []
	# node_names = []

	parent_names = []
	child_names = []

	with open('day6.txt', 'r') as f:
		for line in f:
			l = line.rstrip().split(')')
			parent_name = l[0]
			child_name = l[1]
	
			parent = get_node(nodes, parent_name)
			child = get_node(nodes, child_name)


			print("parent", parent)

			if parent:
				print("PARENT HERE")
				if not child:
					child = Node(name=child_name, parent=parent)
					print("creating child", child, "with parent: ", child.parent, "!")
					print("this node has {} orbits".format(child))
					nodes.append(child)
					print("xxx")
			else:
				
				parent = Node(name=parent_name)
				
				
				print("creating parent", parent)
				nodes.append(parent)
				if not child:
					child = Node(name=child_name, parent=parent)
					nodes.append(child)

	with open('day6.txt', 'r') as f:
		for line in f:
			l = line.rstrip().split(')')
			parent_name = l[0]
			child_name = l[1]

			parent = get_node(nodes, parent_name)
			child = get_node(nodes, child_name)

			

			if not child.parent:
				i = nodes.index(child)
				nodes[i].parent = parent
				



	# testng
	n = Node(name="com")
	child = Node(name="a", parent=n)
	child_2 = Node(name="b", parent=child)

	print(child_2.no_of_parents())

	print("nodes", nodes)

	total_node_calc = 0
	for node in nodes:
		print("{} has {} orbits".format(node, node.no_of_parents()))
		total_node_calc = total_node_calc+node.no_of_parents()

	# 	if node.name == 'J':
	# 		print("parent of j is: ", node.parent)
	# 		print("grandparent of j is: ", node.parent.parent)

	# print(get_node(nodes, 'VQJ').parent)

	# print(get_node(nodes, '5BK').parent)

	print(len(nodes))


	print(total_node_calc)

main()
