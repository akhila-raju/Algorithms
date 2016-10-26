# def bfs(node):

# def dfs(node):

# def binarySearch():



# def quicksort():

# def inOrder():

# def mergesort():

# def reverseStr():


class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next		

def isCycle(node):
	if node == None:
		return False
	else:
		if node.next != None:
			isCycle(node.next)
		if node.next.next != None:
			isCycle(node.next.next)
		return True

Node3 = Node(3, None)
Node2 = Node(2, Node3)
Node1 = Node(1, Node2)
