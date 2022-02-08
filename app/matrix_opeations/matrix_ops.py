from numpy import genfromtxt, matrix, ndarray, array2string
from pandas import DataFrame

class MatrixOperators():
    
    def __init__(self, csv_file=None):
        """
        Build this objects require a csv_file, but 
        methods are independent of self file matrix created
        """
        self.matrix = None 
        self.array=None
        if csv_file:
            self.get_from_csv(input_file=csv_file)

    def get_from_csv(self, input_file, delimiter=',', dtype=int)->matrix:
        """
        Read CSV file and return a numpy matrix object 
        """
        try:
            self.matrix = genfromtxt(input_file, delimiter=delimiter, dtype=dtype)
            return self.matrix
        except Exception as e:
            print(e)
            return e
    
    def print(self, array=None)->str:
        """
        This method returns a string from a matrix or vector
        """
        df = DataFrame(array)
        return df.to_html(header=False, index=False)

    def invert(self, matrix=None)->matrix:
        """
        This name is cause readme but in really returns a transpose of matrix
        """
        if not matrix:
            matrix = self.matrix
        return matrix.transpose()

    def flatten(self, matrix=None)->ndarray:
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
        return int(matrix.cumsum()[-1])
        

    def multiply(self, matrix=None)->int:
        """
        This method return a cumulative multiplication of elements on a matrix
        """
        if not matrix:
            matrix  = self.matrix
        return int(matrix.cumprod()[-1])

