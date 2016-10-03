# 1.1
def isUnique(word):
	for l1 in word:
		for l2 in word:
			if l1 == l2:
				return False
	return True

# 1.2
def isPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	str1 = sorted(str1)
	str2 = sorted(str2)
	for i in len(str1):
		if str1[i] != str2[i]:
			return False
	return True

# ch 4 implementation



# finding 3 numbers that add to a number
# finding the kth smallest index in a rotated array -- can be done linear time

