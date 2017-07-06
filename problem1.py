# This is my solution to Problem 1, 3 functions that compute the sum of the numbers in a list using a for-loop, while-loop, and recursion

# sum using for loop
def forSum(list):
	sum = 0
	for i in range(len(list)):
		sum += list[i]
	return sum
	
# sum using while loop
def whileSum(list):
	sum = 0
	i = 0
	while i < len(list):
		sum += list[i]
		i += 1
	return sum
	
# sum using recursion
def recSum(list):
	sum = 0
	if len(list) > 1:
		sum = recSum(list[:-1]) + list[-1]
	else:
		sum = list[0]
	return sum

a = [34321, 32, 1, 0, 23]
print(forSum(a))
print(whileSum(a))
print(recSum(a))