import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I


def dot_product(vector_A, vector_B):
    """
    Returns the dot product of two vectors
    
    """
    result = 0    
    for i in range(len(vector_A)):
        result += vector_A[i] * vector_B[i]
    return result 
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            det = self[0][0]
        if self.h == 2:
            det = self[0][0] * self[1][1] - self[0][1] * self[1][0]
        return det
     

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        tra = 0
        for i in range(self.h):
            tra += self[i][i]
        return tra

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here         
        det = self.determinant()
        
        if self.h == 1:
            inv = [[1/det]]
        elif self.h == 2:
            inv = [[0, 0],[0,0]]
            inv[0][0] = self[1][1]/det
            inv[0][1] = -self[0][1]/det
            inv[1][0] = -self[1][0]/det
            inv[1][1] = self[0][0]/det
        else:
            inv = None    
        return Matrix(inv)        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for i in range(self.w):
            row =[]
            for j in range(self.h):
                row.append(self[j][i])
            transpose.append(row)
        return Matrix(transpose)   
     

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            result.append(row)
        return Matrix(result)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1.0 * self[i][j])
            result.append(row)
        return Matrix(result)
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        result = []
        other_transpose = other.T()
        for i1 in range(self.h):
            row = []
            for i2 in range(other_transpose.h):
                dp = dot_product(self[i1], other_transpose[i2])
                row.append(dp)            
            result.append(row)

        return Matrix(result)     
       

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            # pass
            #   
            # TODO - your code here
            #
            result = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other * self[i][j])
                result.append(row)
            return Matrix(result)
        else:
            raise(ValueError, "The thing on the left of the * is not a number.")       
                    