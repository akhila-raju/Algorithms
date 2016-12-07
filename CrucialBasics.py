# def bfs(node):
import deque
def bfs(graph, node):
	visited, queue = [], deque(node)
	while queue:
		node = queue.popleft()
		if node not in visited:
			visited.append(node)
			for adjacent in graph[node]:
				queue.append(adjacent)
	return visited

# def dfs(node):
def dfs(graph, node):
	visited, stack = [], deque(node)
	while stack:
		node = queue.pop()
		if node not in visited:
			visited.append(node)
			for adjacent in graph[node]:
				stack.append(adjacent)
	return visited

# def binarySearch():
def binarySearch(arr, x):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high) // 2
		if x < arr[mid]:
			high = mid - 1
		elif x > arr[mid]:
			low = mid + 1
		else:
			return mid


# def quicksort():
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


# def inOrder():
def inOrder(node):
	if node == Null:
		return []
	return inOrder(node.left) + node.val + inOrder(node.right)


# def mergesort():
def mergesort(arr): 
	if len(arr) > 1:
		pivot = len(arr) // 2
		lo = quicksort(arr[:pivot])
		hi = quicksort(arr[pivot:])
		return merge(lo, hi)
	else:
		return arr

def merge(lo, hi):
	if not lo:
		return hi
	elif not hi:
		return lo
	elif lo[0] < hi[0]:
		return [lo[0]] + merge(lo[1:], hi)
	else:
		return [hi[0]] + merge(lo, hi[1:])

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


# hash table representation using a list of lists
class HashTable: 
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.list = [[] for x in range(num_buckets)]
    def hash(self, key): 
        return key % self.num_buckets
    def insert(self, key, val): 
        index = self.hash(key)
        bucket = self.list[index]
        self.list[index].append((key, val))
    def remove(self, key, val): 
        index = self.hash(key)
        bucket = self.list[index]
        for item in bucket: 
            if item[1] == val: 
                bucket.remove(item)
    def __repr__(self): 
        return repr(self.list)

h = HashTable(10)
print(h)
h.insert(5, "apple")
h.insert(5, "pear")
print(h)
h.remove(5, "apple")
print(h)