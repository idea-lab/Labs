def functionname(arguments):
	#do something with arguments
	return #return a value or just end

def add(a, b):
	return a+b
 

def main():
	print (add(1, 6))

	#Lambdas/Anonymous functions
	mult = lambda x, y: x*y
	print(mult(2, 5))

	#functions are also variables

	copyOfAdd=add

	print(copyOfAdd(2, 5), "\n")

	operations = [add, lambda x, y: x-y, mult, lambda x, y: x/y]

	for i in operations:
		print(i(2,3))

main()