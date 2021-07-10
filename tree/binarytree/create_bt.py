from collections import deque

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
# print('-----Root Node initialization---------')
# Time: O(1) Space: O(1)
bt = TreeNode('Drinks')

cold = TreeNode('cold')
hot = TreeNode('hot')
bt.left = cold
bt.right = hot

tea = TreeNode('Tea')
cofee = TreeNode('cofee')
hot.left = tea
hot.right = cofee

pepsi = TreeNode('pepsi')
cola = TreeNode('cola')
cold.left = cola
cold.right = pepsi

print('-----PreOrder TRAVERSAL---------')
# Time: O(n/2) + O(n/2) = O(n)
# Space: We are using stack memory
def pre_order_traversal(root_node):
	if not root_node:
		return
	# root -> left -> right
	print(root_node.data) # O(1)
	pre_order_traversal(root_node.left) # O(n/2)
	pre_order_traversal(root_node.right) # O(n/2)

pre_order_traversal(bt)

print('-----InOrder TRAVERSAL---------')
# Time: O(n/2) + O(n/2) = O(n)
# Space: We are using stack memory
def inorder_traversal(root_node):
	if not root_node:
		return 
	# left -> root -> right
	inorder_traversal(root_node.left) # O(n/2)
	print(root_node.data) # O(1)
	inorder_traversal(root_node.right) # O(n/2)

inorder_traversal(bt)

print('-----PostOrder TRAVERSAL---------')
# Time: O(n/2) + O(n/2) = O(n)
# Space: We are using stack memory
def post_order_traversal(root_node):
	if not root_node:
		return 
	# left -> right -> root
	post_order_traversal(root_node.left) # O(n/2)
	post_order_traversal(root_node.right) # O(n/2)
	print(root_node.data) # O(1)

post_order_traversal(bt)


print('-----LevelOrder TRAVERSAL---------')
# Time: O(n) and Space: O(n)
def leve_order_traversal(root_node):
	if not root_node:
		return 
	else:
		Queue = deque()
		Queue.append(root_node)
		while len(Queue) > 0:
			root = Queue.popleft()
			print(root.data)
			if root.left is not None:
				Queue.append(root.left)
			if root.right is not None:
				Queue.append(root.right)

leve_order_traversal(bt)