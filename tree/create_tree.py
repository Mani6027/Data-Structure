class TreeNode:
	def __init__(self, data, children=[]):
		self.data = data
		self.children = children
	
	def __str__(self, level=0):
		ret = "	" * level + str(self.data) + "\n"
		for child in self.children:
			ret += child.__str__(level + 1) 
		return ret
	
	def add_child(self, TreeNode):
		self.children.append(TreeNode)

root = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
root.add_child(cold)
root.add_child(hot)
cola = TreeNode('cola', [])
pepsi = TreeNode('fanta', [])
cofee = TreeNode('cofee', [])
tea = TreeNode('tea', [])
cold.add_child(cola)
cold.add_child(pepsi)
hot.add_child(tea)
hot.add_child(cofee)
print(root)