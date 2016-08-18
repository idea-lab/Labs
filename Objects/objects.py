class Person:
	def __init__(self, age, name):
		self.age=age
		self.name=name
	def getAge(self):
		return self.age
	def getName(self):
		return self.name

class Animal:
	def __init__(self):
		

a = Person(10, "hi")

print(a.getAge())
print(a.getName())