"""
The 2D array creation functions e.g. numpy.eye, numpy.diag, and numpy.vander
define properties of special matrices represented as 2D arrays.
"""
import numpy as np

"""
np.eye(n, m) defines a 2D identity matrix(单位矩阵). 
The elements where i=j (row index and column index are equal) 
are 1 and the rest are 0.
"""
a2D_1 = np.eye(3)
a2D_2 = np.eye(3, 5)
print(f"a2D_1:\n{a2D_1}\n")
print(f"a2D_2:\n{a2D_2}\n")

"""
numpy.diag can define either a square(方形) 2D array with given values along the diagonal(对角)
or if given a 2D array returns a 1D array that is only the diagonal elements. 
The two array creation functions can be helpful while doing linear algebra.
"""
a2D_3 = np.diag([1, 2, 3])
print(f"a2D_3:\n{a2D_3}\n")
a2D_4 = np.diag([1, 2, 3], 3)
print(f"a2D_4:\n{a2D_4}\n")
a2D_5 = np.array([[1, 2], [3, 4]])
print(f"a2D_5:\n{a2D_5}\n")

"""
vander(x, n) defines a Vandermonde matrix as a 2D NumPy array. 
Each column of the Vandermonde(范德蒙德) matrix is a decreasing power of 
the input 1D array or list or tuple, 
x where the highest polynomial order is n-1. 
"""
a2D_6 = np.vander(np.linspace(0, 2, 5), 2)
print(f"a2D_6:\n{a2D_6}\n")
a2D_7 = np.vander([1, 2, 3, 4], 2)
print(f"a2D_7:\n{a2D_7}\n")
a2D_8 = np.vander((1, 2, 3, 4), 4)
print(f"a2D_8:\n{a2D_8}\n")
