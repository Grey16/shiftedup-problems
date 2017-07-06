# This is my solution to Problem 2, combining 2 lists by alternating and taking elements from each list.
def mergeList(a, b):
	if len(a) != len(b):
		return null
	c = list()
	for i in range(len(a)):
		c.append(a[i])
		c.append(b[i])
	return c
	
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(mergeList(a, b))
