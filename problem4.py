# This is my solution to Problem 4, rearranging the numbers in a list to form the largest possible number

def bigNum(a):
	newList = list()
	# turn numbers into strings
	for i in range(len(a)):
		a[i] = str(a[i])
	# rearrange list in decreasing order based on first digit
	for i in range(9, 0, -1):
		for j in range(len(a)):
			if a[j][0] == str(i):
				newList.append(a[j])
	return newList
a = [9, 3, 1, 2, 50, 60]
print(bigNum(a))