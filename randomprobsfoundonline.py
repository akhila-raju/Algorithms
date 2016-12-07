def hasTarget(arr, n):
    set_ = set()
    for elem in arr:
        set_.add(elem)
        n_e = n - elem
        if n_e in set_:
            return True
    return False

def hasTarget_n(arr, n):
    for elem in arr:
        hasTarget = binarySearch(arr, n-elem)
        if hasTarget:
            return True
    return False
    
def binarySearch(arr, n):
    # returns index of item we want
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if n < arr[mid]:
            high = mid - 1
        elif n > arr[mid]:
            low = mid + 1
        else:
            return True

print(hasTarget_n([2,4,5,9,1], 7))


