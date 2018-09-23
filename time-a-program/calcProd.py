import time
def calcProd():
#calculate the product of the first 100,000 numbers.

	product = 1
	for i in range(1,100000):
		product = product * i
	return product

startTime = time.time() # We set the start time before running the function.
prod = calcProd()
endTime = time.time() # We grab the end time after the function is returned.

print('The result is %s digists long.' % (len(str(prod))))

print('It took %s seconds to calculate.' % ( endTime - startTime))



