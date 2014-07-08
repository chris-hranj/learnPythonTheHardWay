
numbers = []

def looper(loopSize):
	i = 0
	for num in range(i, loopSize):
		print "At the top i is %d" % i
		numbers.append(i)

		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

looper(20)
