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
    def __neg__(self):
        return Vector([])


    # Implement this function
    def __sub__(self, other):

        return Vector([])
