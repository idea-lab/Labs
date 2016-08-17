#LOOPS

#while loops
x=0
while(x<10):
	x = x+1
	print(x)
#for loops
for y in range(0, 10):
	print(y)
#for loops going down
for i in range(10, 0, -1):
	print(i)
print("\n")
#looping through elements of a list
myList=[2, 3, 5, 1, 7]

for i in myList:
	print(i)

#IF/ELSE
if 1 == 1:
	print("true")
elif 2==2:
	print("also true")
else:
	print("false")