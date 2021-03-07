### Create an iterator class that returns n fibonacci numbers ###
class Fibonacci():
	fibonacci_cache = {0:0, 1:1, 2:1} # Class var for the fib numbers we have already calculated
	def __init__(self,n):
		self.n = n
		value = self.n
		self.fibs = [Fibonacci.fibonacci_memo(num) for num in range(0, n)]
		self.index = 0
		
		

		


	def __iter__(self):
		return self

	def __next__(self):
		if self.n > 0: #termination condition
			current_num = self.fibs[self.index]
			self.n -= 1
			self.index += 1
			return current_num
		else:
			raise StopIteration



		



	@classmethod
	def fibonacci_memo(cls,input_value):

		if input_value in Fibonacci.fibonacci_cache:
			return Fibonacci.fibonacci_cache[input_value]
		if input_value == 1:
			value = 1
		elif input_value == 2:
			value = 1
		elif input_value > 2:
			value = Fibonacci.fibonacci_memo(input_value - 1) + Fibonacci.fibonacci_memo(input_value - 2)
			Fibonacci.fibonacci_cache[input_value] = value
		return value




##Driver Code##
if __name__ == '__main__':
	my_fib = Fibonacci(7)
	my_iter = iter(my_fib)
	for x in my_iter:
		print(x)
