# bfs
import deque
def bfs(graph, node):
	visited, queue = [], deque()
	while queue:
		node = queue.popleft()
		if node not in visited:
			visited.append(node)
			for adjacent in graph[node]:
				queue.append(adjacent)
	return visited

# dfs
def dfs(graph, node):
	visited, stack = [], deque()
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			for adjacent in graph[node]:
				stack.append(adjacent)
	return visited

# quicksort
import random
def quicksort(arr):
	if len(arr) > 1:
		less, equal, more = [], [], []
		pivot = random.choice(arr)
		for item in arr:
			if item < pivot:
				less.append(item)
			elif item > pivot:
				more.append(item)
			else:
				equal.append(item)
		return quicksort(less) + equal + quicksort(more)
	else:
		return arr

# binary search
def binarySearch(arr, x):
	lo = 0
	hi = len(arr) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if x < arr[mid]:
			hi = mid - 1
		elif x > arr[mid]:
			lo = mid + 1
		else:
			return mid

# tree construction
class Node:
	def __init__(self, val, left=None, right=None, parent=None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

# tree traversal
def preOrder(node):
	if node == None:
		return []
	return node.val + preOrder(node.left) + preOrder(node.right)

def inOrder(node):
	if node == None:
		return []
	return inOrder(node.left) + node.val + inOrder(node.right)

def postOrder(node):
	if node == None:
		return []
	return postOrder(node.left) + postOrder(node.right) + node.val


