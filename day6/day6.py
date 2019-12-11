import datetime

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

def commonAncestor(basenode, node):
		if not node:
			return None

		if node.parent == basenode:
			return node.parent

		return commonAncestor(basenode, node.parent)

def get_node_length(parent_node, child_node, length=0):
		if parent_node == child_node:
			return length
		return get_node_length(parent_node, child_node.parent, length=length+1)

def main():
	nodes = []

	parent_names = []
	child_names = []

	with open('day6.txt', 'r') as f:
		for line in f:
			l = line.rstrip().split(')')
			parent_name = l[0]
			child_name = l[1]
	
			parent = get_node(nodes, parent_name)
			child = get_node(nodes, child_name)

			if parent:
				if not child:
					child = Node(name=child_name, parent=parent)
					nodes.append(child)
			else:
				
				parent = Node(name=parent_name)
				
				nodes.append(parent)
				if not child:
					child = Node(name=child_name, parent=parent)
					nodes.append(child)

	with open('day6.txt', 'r') as f:  # todo use hash map instead of this
		for line in f:
			l = line.rstrip().split(')')
			parent_name = l[0]
			child_name = l[1]

			parent = get_node(nodes, parent_name)
			child = get_node(nodes, child_name)

			if not child.parent:
				i = nodes.index(child)
				nodes[i].parent = parent

	total_node_calc = 0
	for node in nodes:
		total_node_calc = total_node_calc+node.no_of_parents()

	san = get_node(nodes, 'SAN')
	you = get_node(nodes, 'YOU')


	common_ancestor = None
	parent_of_san = san.parent

	while not common_ancestor:
		common_ancestor = commonAncestor(parent_of_san, you)
		parent_of_san = parent_of_san.parent

	def get_node_length(parent_node, child_node, length=0):
		if parent_node == child_node:
			return length
		return get_node_length(parent_node, child_node.parent, length=length+1)

	san_to_ancestor = get_node_length(common_ancestor, san)-1
	you_to_ancestor = get_node_length(common_ancestor, you)-1

	answer = san_to_ancestor + you_to_ancestor

	print("no is: ", answer)

main()