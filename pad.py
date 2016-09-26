#STARTING STUFF

#printing
print("Hello Caleb")
print(200)

#math and order of operations
print(3 + 5 * 10 /2)

#modulo
print(10 % 3)



#SIMPLE VARIABLES (numbers)

#declaring and initializing variables
x = 10
print(x)

#reassigning variables
x = 15
print(x)

#using variables
y = x + 10
print(y)

#incrementing variables
x = x + 3
print(x)



#STRINGS

#assigning strings
name = "Caleb"
print(name)

#String concatenation
print("py" + "thon")
print(name + " Trotz")

#characters at specific positions (ZERO INDEX)
print(name[0])
print(name[2])
print(name[0:3])
print(name[1:4])

#practice: Create a string that stores a sentence and print out the first two
#     words of the sentence using string splicing.

sentence = "This is a sentence."
print(sentence[0: 7])



#BOOLEANS

#declaring booleans (True and False)
isFriday = True
isRaining = False

#and, or operators
print(True and False)
print(True or False)
print(isFriday and isRaining)
print(isFriday or isRaining)



#LISTS

#creating lists
numbers = [10, 20, 30, 40, 50, 60]
print(numbers)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

#accessing specific values (ZERO INDEX)
print(numbers[0])
print(numbers[3])
print(names[2])

#changing specific values
numbers[3] = 100
print(numbers)
names[2] = "Caleb"
print(names)

#array slicing (python specific)
print(numbers[2:4])
print(numbers[:4])
print(names[1:4])
print(names[:3])

#practice: Create a list that stores 7 numbers and print out the middle 3
#     numbers.


#LOOPS

#while loops
x = 0
while (x < 10):
      print(x)
      x = x + 1

#practice: Use a while loop to print all the odd numbers between 0 and 20.
odd = 1
while (odd < 20):
      print(odd)
      odd = odd + 2

#for loops
for y in range(0, 10):
      print(y)

#for loops going down
for i in range(10, 0, -1):
      print(i)

#iterating over elements of a list
newList = [2, 3, 5, 1, 7]

for i in newList:
      print(i)

#practice: Use a for loop to print all the odd numbers between 0 and 20.
for odd in range(0, 20):
      print(odd)
      odd = odd + 2
      


#CONDITIONALS

#if, else
x = 5
if (x == 5):
      print("x is 5")
else:
      print("x is not 5")

#practice: Write a set of conditionals checking whether a number is even or odd.
number = 0
if (number %2 == 1):
      print("number is odd")
else:
      print("number is even")

#if, elif, else
x = 5
if (x == 5):
      print("x is 5")
elif (x == 6):
      print("x is 6")
else:
      print("x is neither 5 nor 6")

#practice: Write a set of conditionals to find the larger of two numbers. Print
#     out the larger number. If they're equal, say so.
num1 = 1
num2 = 2
if (num1 > num2):
      print(num1)
elif (num2 > num1):
      print(num2)
else:
      print("equal")
      


#USER INPUT

#input function
name = input("What is your name? ")

#stuff you can do with input
if (name == "Caleb"):
      print("...")
else:
      print("Hello " + name + ".")
