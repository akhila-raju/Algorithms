arr = [7, 3, 9, 5]

def insertionSort(arr):
	# starting at the left side, sort in place.
	return




def selectionSort(arr): # O(n^2)
    # walk through list and find the smallest item, append to the end of the sorted part.
    for i in range(len(arr)):
        least = i # current element to swap with
        for k in range(i+1, len(arr)): # because we always add the smallest item in order
            if arr[k] < arr[least]: # if the element we are checking is smaller than our min so far,
                least = k # change min
        # swap elements
        tmp = arr[least]
        arr[least] = arr[i]
        arr[i] = tmp

    return arr
# test
arr = [7, 3, 9, 5]
print(selectionSort(arr))




# good for data structures with constant access time
import random
def quickSort(arr): # O(nlogn) usually, O(n^2) worst case
    if len(arr) > 1:
        less, equal, more = [], [], []
        pivot = random.choice(arr) # choose random pivot to avoid case where list is already sorted (O(n^2))

        for x in arr:
            if x < pivot:
                less.append(x) # appending is constant time
            elif x > pivot:
                more.append(x)
            else:
                equal.append(x)

        return quickSort(less) + equal + quickSort(more)
    else:
        return arr
    
arr = [7, 3, 9, 5, 13, 11]
print arr
print(quickSort(arr))




# better for data structures without constant access time
def mergeSort(arr):
    if len(arr) > 1:
        pivot = len(arr) // 2
        less = mergeSort(arr[:pivot])
        more = mergeSort(arr[pivot:])
        return merge(less, more)
    else:
        return arr

def merge(less, more):
    if not less: # checks if empty list
        return more
    elif not more: # checks if empty list
        return less
    elif less[0] < more[0]:
        return [less[0]] + merge(less[1:], more) # put smallest item first, build up
    else:
        return [more[0]] + merge(less, more[1:])

arr = [7, 3, 9, 5, 13, 11]
print(mergeSort(arr))
