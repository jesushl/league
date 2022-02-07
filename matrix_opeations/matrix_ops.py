from msilib.schema import Error
from numpy import genfromtxt, matrix, ndarray, array2string


class MatrixOperators():
    def __init__(self, csv_file):
        self.matrix = None 
        self.array=None
        self.get_from_csv(input_file=csv_file)

    def get_from_csv(self, input_file, separator=',', dtype=int)->matrix:
        """
        Read CSV file and return a numpy matrix object 
        """
        try:
            self.matrix = genfromtxt(input_file, separator=separator, dtype=dtype)
            return self.matrix
        except Error as e:
            print(e)
            return e
    
    def print(self, array=None)->str:
        """
        This method returns a string from a matrix or vector
        """
        return array2string(array)

    def invert(self, matrix=None)->matrix:
        """
        This name is cause readme but in really returns a transpose of matrix
        """
        if not matrix:
            matrix = self.matrix
        return matrix.transpose()

    def fatten(self, matrix=None)->ndarray:
        """
        This method return an array from a matrix
        """
        if not matrix:
            matrix = self.matrix
        return matrix.flatten()

    def sum(self, matrix=None)->int:
        """
        This method return the cumulative sum of elements on a matrix
        """
        if not matrix:
            matrix  = self.matrix
        return matrix.cumsum()[-1]
        

    def multiply(self, matrix=None)->int:
        """
        This method return a cumulative multiplication of elements on a matrix
        """
        if not matrix:
            matrix  = self.matrix
        return matrix.cumprod()[-1]

