# Reverse a linked list.
class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt
        
# iterative
def reverse_1(node):
    if node == None:
        return
    prev = None
    curr = node
    while curr:
        tmp = curr.nxt # move along linked list
        curr.nxt = prev # reversal
        prev = curr # reversal
        curr = tmp # move along linked list
    return prev

# recursive
def reverse_2(n, last=None):
    if n == None:
        return last
    nxt = n.nxt # move along linked list
    n.nxt = last # reversal
    return reverse_2(nxt, n)

def prnt(n):
    nxt = n.nxt
    print n.val
    if nxt is not None:
        prnt(nxt)

# test
Node3 = Node(3, None)
Node2 = Node(2, Node3)
Node1 = Node(1, Node2)

print "Original list"
prnt(Node1)

nr1 = reverse_1(Node1)
print "Reversed list iterative"
prnt(nr1)

print "Reversed N recursive"
nr2 = reverse_2(nr1)
prnt(nr2)




# Reverse a string.
def reverseString(str):
	# Create an array. 
	newString = []
	# Insert the string in a reverse order by accessing indeces reversely. 0 indexed
	index = len(str) - 1
	# Insert reversely.
	while index >= 0:
		newString.append(str[index])
		index -= 1
	print ''.join(newString)

def reverseString_2(str):
	return str[::-1]
# test case
reverseString("hello")
reverseString_2("hello")




# Give the nth fibonacci number, recursively and iteratively.
# Recursively, O(2^n)
def fib_r(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
# Iteratively, O(n)
def fib_i(n):
	index = n
	sum_ = 0
	while index < 0:




# Check if a word is a palindrome.
def isPalindrome_1(word):
    first = len(word) - 1
    last = 0
    while first != last: # constant time
        if word[first] != word[last]:
            return False
        first -= 1
        last += 1
    return word[first] == word[last]

def isPalindrome_2(word):
	return word == word[::-1]
# test
test1 = isPalindrome_1("rainbow")
test2 = isPalindrome_2("mom")
print(test1)
print(test2)