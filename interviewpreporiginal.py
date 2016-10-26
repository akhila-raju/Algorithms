#
#	REVERSE A LINKED LIST.
#
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




#
#	REVERSE A STRING
#
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




#
#	GIVE THE NTH FIBONACCI NUMBER, RECURSIVELY AND ITERATIVELY.
#
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




#
#	CHECK IF A WORD IS A PALINDROME.
#
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




#
#	REVERSE AN INTEGER. (Do not use a string)
#
# 123 --> 321
def reverseInt(n):
	# 123 % 10 = 3
	reverse = 0
	while n > 0:
		remainder = n % 10 # 3
		reverse = reverse * 10 + remainder
		n = n // 10 # move left in original integer
	return reverse
#test
print(reverseInt(12345))




#
#	GIVEN A STRING, RETURN AN INT REPRESENTATION. GIVEN AN INT, RETURN A STRING REPRESENTATION.
#
def intToStr(int):
    return str(int)

def strToInt(str):
    return int(str)

n = 123
print (intToStr(n))
print (type(intToStr(n)) == str)
print (strToInt(n))
print (type(strToInt(n)) == int)




# Suppose we have an array with increasing integers and at some point they start 
# decreasing. Write a method to return the max integer
# [0, 1, 2, 3, 6, 7, 10, 8, 5, 4] ==> 10  (aim for logn time)
# assume no repeats
# binary search
def findMax(arr):
	
	return




# longest common subsequence - dynamic programming

# longest common substring - dynamic programming

# max sum in an array of numbers

# finding 3 numbers that add to a number

# finding the kth smallest index in a rotated array -- can be done linear time










