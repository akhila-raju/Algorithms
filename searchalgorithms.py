# binary search
# array must be sorted for this to work
def binarySearch(arr, val):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        elif val < arr[mid]:
            hi = mid - 1
        else:
            return mid
    return None
# test
print(binarySearch([1,5,8,10], 5))


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

def dfs(graph, start):
	visited, stack = set(), [start]