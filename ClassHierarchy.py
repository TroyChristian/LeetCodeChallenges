from abc import ABC, abstractmethod

#Define an abstract base class Shape, that Square and Rectangle will inherit from
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

	@classmethod
	@abstractmethod
	def get_endpoints():
		pass

	@classmethod
	@abstractmethod
	def get_count(self):
		pass

	@staticmethod
	@abstractmethod
	def information(self):
		pass

class Square(Shape):
	count = 0
	endpoints = 4

	def __init__(self,length):
		self.length = length
		Square.count += 1
	def area(self):
		return self.length * self.length
	def perimeter(self):
		return 4 * self.length

	@classmethod
	def get_endpoints(cls):
		return "There are {} endpoints in a square.".format(Square.endpoints)

	@classmethod
	def get_count(cls):
		return Square.count 

	@staticmethod
	def information():
		return "Hi! I'm a square!"

@Shape.register
class Rectangle():
	count = 0
	endpoints = 4

	def __init__(self, height, length):
		self.length = length
		self.height = height
		Rectangle.count += 1

	def area(self):
		return self.length * self.height

	def perimeter(self):
		return 2*(self.length + self.height)

	@classmethod
	def get_endpoints(cls):
		return "There are {} endpoints in a Rectangle.".format(Rectangle.endpoints)

	@classmethod
	def get_count(cls):
		return Rectangle.count 

	@staticmethod
	def information():
		return "Hi! I'm a Rectangle!"


###Driver Code###
if __name__ == '__main__':
	rectangle = Rectangle(2,4)
	print(rectangle.area())
	print(rectangle.perimeter())
	print(rectangle.get_endpoints())
	print(rectangle.information())







