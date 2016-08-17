# calling a function from itself
# used when a problem can be broken down into repeatable steps
# 2 major parts
# Base case -- the end case of recursion
# Recursing -- self-calling
def fibo(n):
	if(n<=2):
		return 1
	return fibo(n-1)+fibo(n-2)

def main():
	for i in range(0, 10):
		print(fibo(i))


main()