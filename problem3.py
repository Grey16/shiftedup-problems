# This is my solution to Problem 3, computing the sum of the first 100 Fibonacci numbers
# Putting all the numbers in a list probably wasn't the best way to go about it, but it gets the job done

def fibSum():
	a = list()
	sum = 1
	for i in range(100):
		if i == 0:
			a.append(0)
		elif i == 1:
			a.append(1)
		else:
			num = a[i - 1] + a[i - 2]
			a.append(num)
			sum += num
	return sum
	
print(fibSum())