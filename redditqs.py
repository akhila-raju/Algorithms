# Find the most frequent integer in an array
def freqInt(arr):
    d = {}
    for item in arr:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    print(d)
    mosFreq = (None, None)
    for key, val in d.items():
        if val > mosFreq[1]:
            mosFreq = (key, val)
    return mosFreq[0]

array = [0, 1, 1, 3, 4, 2, 4, 2, 1]
print(freqInt(array))


# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)



# Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array. Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}



# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fibiter(n):
    if n < 2:
        return n
    n_2 = 0
    n_1 = 1
    for i in range(2, n):
        n_ = n_2 + n_1
        n_2 = n_1
        n_1 = n_
    return n_2 + n_1

def fibmemo(n):
    if n < 2:
        return n
    memo = []
    memo.append(0)
    memo.append(1)
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n-1] + memo[n-2]

print(fib(25) == fibiter(25) == fibmemo(25))

def fibrecursivememo(n,memo_dict = dict()):
    # Write your code here.
    if n in memo_dict.keys():
        return memo_dict[n]
    elif n < 2:
        memo_dict[n] = n
        return n
    val = fibrecursivememo(n-1,memo_dict) + fibrecursivememo(n-2,memo_dict)
    memo_dict[n] = val
    return memo_dict[n-1] + memo_dict[n-2]
n = int(input())
print(fibrecursivememo(n))



# Find the only element in an array that only occurs once.



# Find the common elements of 2 int arrays


# Implement binary search of a sorted array of integers.
# Binary search finds the position of a target value within a sorted array.
arr = [1, 2, 2, 5, 7, 9]

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
    return None
        
print(binarySearch(arr, 7))
print(binarySearch(arr, 4))


# Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})



# Use dynamic programming to find the first X prime numbers
# 2, 3, 5, 7, 11, 13, etc
# We know that a number is prime if 
def firstPrimes(x):
    if x < 1:
        return
    primes = [2]
    index = 2
    while len(primes) < x:
        index += 1
        if isPrime(index, primes):
            primes.append(index)
    return primes

def isPrime(x, arr):
    for prime in arr:
        if x % prime == 0:
            return False
    return True

print(firstPrimes(25))

# Write a function that prints out the binary form of an int
# example: 5 = 0101. 5 % 2 = 1. 1 * 10 = 10 + 1 %co
# 5 % 2 = 1. bin = 1. n = 2
# 13 % 2 = 1. 13/2 = 6. 6 % 2 = 0.
def binary(n):
    if n == 0:
        return ''
    return binary(n/2) + str(n%2)

print(binary(5))


# Implement parseInt


# Implement squareroot function


# Implement an exponent function (bonus: now try in log(n) time)


# Write a multiply function that multiples 2 integers without using *
def mult(x, y):
    sum_ = 0
    for i in range(1, y+1):
        sum_ += x
    return sum_

print(mult(4, 5))


# HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()


# HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)


# Find the first non-repeated character in a String


# Reverse a String iteratively and recursively
def reverseIter(strng):
    newStr = ''
    index = len(strng)
    while index > 0:
        index -= 1
        newStr += strng[index]
    return newStr

def reverse(strng):
    if strng == '':
        return ''
    return reverse(strng[1:]) + strng[0]

print(reverseIter("python"))
print(reverse("python"))

# Determine if 2 Strings are anagrams


# Check if String is a palindrome


# Check if a String is composed of all unique characters
def uniqueCh(strng):
	from collections import Counter
	c = Counter()
	[c.update({letter}) for letter in strng] # creates an iterator
	for val in c.values():
		if val > 1:
			return False
	return True

def uniqueCh2(strng):
	from collections import Counter
	assert len(strng) > 1, "EMPTY STRING"
	c = Counter()
	[c.update({letter}) for letter in strng] # creates an iterator
	return c.most_common(1)[0][1] == 1 # most_common(1) returns most common of len 


# Determine if a String is an int or a double


# HARD: Find the shortest palindrome in a String


# HARD: Print all permutations of a String


# HARD: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)' that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words; the first word on each line is flushed left and the last word on each line is flushed right


# Implement a BST with insert and delete functions
class Node:
	def __init__(self, val, left=None, right=None, parent=None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

class BST:
	def __init__(self, root):
		self.root = root
	# def insert(self, node):
	# 	if node.val < self.root.val:


# Print a tree using BFS and DFS
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
    
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node in visited:
        return
    visited.append(node)
    for adjacent in graph[node]:
        if adjacent not in visited: 
            dfs(graph, adjacent, visited)
    return visited

def dfs_paths(graph, start, target, path=None):
    if path == None:
        path = [start]
    if start == target:
        yield path
    for vertex in [x for x in graph[start] if x not in path]:
        for each_path in dfs_paths(graph, vertex, target, path + [vertex]):
            yield each_path

def dfs_paths(graph, start, target):
    stack = dequeue( [ (start, [start]) ] )
    while stack:
        node = stack.pop()
        for adjacent in graph[node[0]]:
            if adjacent not in node[1]:
                if node == target:
                    yield graph[node[1]] + [node]
                else:
                    stack.append( (node, graph[node[1]] + [node]) )

            
from collections import deque
def bfs(graph, node):
    visited, queue = [], deque(node)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for adjacent in graph[node]:
                queue.append(adjacent)
    return visited

def bfs_paths(graph, start, target):
	# (node, path)
    queue = deque( [ (start, [start]) ] )
    while queue:
    	# last in first out
        vertex_path = queue.popleft()
        # check if node is already in path
        for node in [x for x in graph[vertex_path[0]] if x not in vertex_path[1]]:
            # add node to path
            if node == target:
                yield vertex_path[1] + [node]
            else:
                queue.append( (node, vertex_path[1] + [node]) )

def shortest_path(graph, start, target):
    return next(bfs_paths(graph, start, target))


print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'C'))
print(shortest_path(graph, 'A', 'F'))

# Write a function that determines if a tree is a BST
def isBST(node):
	if node == None:
		return
	if node.left:
		isBST(node.left)
		return node.left.val < node.val
	if node.right:
		isBST(node.right)
		return node.right.val > node.val


# Find the smallest element in a BST
# leftmost
def smallestVal(node):
	if node.left != None:
		return smallestVal(node.left)
	return node.val


# Find the 2nd largest number in a BST
# 0
#  \
#   0
#    \
#     0
#      \
#       0
def secLargest(node):
	if node.right.right != None:
		return secLargest(node.right)
	return node.val

# Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine whether the tree is a valid sum tree


# Find the distance between 2 nodes in a BST and a normal binary tree


# Print the coordinates of every node in a binary tree, where root is 0,0


# Print a tree by levels


# Given a binary tree which is a sum tree, write an algorithm to determine whether the tree is a valid sum tree


# Given a tree, verify that it contains a subtree.


# HARD: Find the max distance between 2 nodes in a BST.


# HARD: Construct a BST given the pre-order and in-order traversal Strings
def preOrder(node): # P L R
	if node == None:
		return []
	return node.val + preOrder(node.left) + preOrder(node.right)

def preOrder(root):
    #Write your code here
    if root != None:
        # print on same line with comma and space
        print(str(root.data), end= " ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(node): # L P R
    if node == None:
        return []
    return inOrder(node.left) + node.val + inOrder(node.right)


def getHeight(self, root, height=0):
    #Write your code here
    if root == None:
        return -1
    else:
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


def check_binary_search_tree_(root):
    # left subtree is less than, right subtree is greater than
    inorder_arr = inOrder(root, [])
    temp = 0
    for item in inorder_arr:
        if item > temp:
            temp = item
        else:
            return False
    return True
    
def inOrder(root, arr):
    if root != None:
        inOrder(root.left, arr)
        arr.append(root.data)
        inOrder(root.right, arr)
    return arr

# Implement a stack with push and pop functions
class Stack:
    def __init__(self, *args):
        self.arr = list(args)
        
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
    def __repr__(self):
        return repr(self.arr)

stack = Stack()
stack.push(5)
stack.push(7)
stack.push(9)
print(stack)
stack.pop()
print(stack)

# Implement a queue with queue and dequeue functions
class Queue_O_n: # n time for dequeue
	def __init__(self, *args):
		self.arr = list(args)
	def enqueue(self, item):
		self.arr.append(item)
	def dequeue(self):
		item = self.arr[0]
		self.arr = self.arr[1:]
		return item
	def __repr__(self):
		return repr(self.arr)

class Queue_O_1: # constant time for dequeue -- pop left and pop right
	from collections import deque
	def __init__(self, *args):
		self.arr = deque(args)
	def enqueue(self, item):
		self.arr.append(item)
	def dequeue(self):
		return self.arr.popleft()
	def __repr__(self):
		return repr(self.arr)

queue = Queue_O_1()
queue.enqueue(5)
print(queue)
print(queue.dequeue())
print(queue)

# Find the minimum element in a stack in O(1) time


# Write a function that sorts a stack (bonus: sort the stack in place without extra memory)


# Implement a binary min heap. Turn it into a binary max heap


# HARD: Implement a queue using 2 stacks


# Implement a linked list (with insert and delete functions)


# Find the Nth element in a linked list


# Remove the Nth element of a linked list


# Check if a linked list has cycles


# Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop


# Check whether a linked list is a palindrome


# Reverse a linked list iteratively and recursively


# Print a linked list in reverse order
def ReversePrint(head):
    if head != None:
        ReversePrint(head.next)
        print(head.data)
        

# Implement bubble sort


# Implement selection sort


# Implement insertion sort


# Implement merge sort


# Implement quick sort
import random
def quickSort(arr):
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
        
        return quickSort(less) + equal + quickSort(more)
    else:
        return arr

arr = [1, 1, 1, 4, 2, 4, 2, 4, 2]
print(quickSort(arr))