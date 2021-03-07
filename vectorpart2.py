import itertools
#Some example methods code provided courtesy of instructor at Educative

class Vector():

    def __init__(self, vector):
        self.vector = vector

    def print(self):
        print(self.vector)

    def __pos__(self):
    	return Vector(self.vector)

    def __add__(self, other):
    	
    	return Vector(i+j for i,j in itertools.zip_longest(self.vector, other.vector, fillvalue=0))
    	

    

    def __mul__(self, scalar):
    	try:
    		return Vector(n * scalar for n in self.vector)
    	except:
    		raise NotImplemented

    def __rmul__(self, scalar):
    	return self * scalar
    

    # Implement this function
    #Expected input format: [1,2] + [-1, 2]
    #Expected input two: "-2i + 3j - 5k"
    #Expeced input actual [2,3]
    def __neg__(self):

        return Vector([-i for i in self.vector])


    # Implement this function
    def __sub__(self, other):
    	try:
    		return Vector([i - j for i,j in itertools.zip_longest(self.vector, other.vector, fillvalue=0)])
    	except:
    		raise NotImplemented

    def __rsub__(self,scalar):
    	return Vector([n - scalar for n in self.vector])


#Driver Code#
v1 = Vector([-2,4,6])
v2 = Vector([4,8,12])

v3 = -v1
print(v3.vector)
