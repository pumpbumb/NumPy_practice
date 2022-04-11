"""
The ndarray creation functions e.g. numpy.ones, numpy.zeros, and random define arrays based upon the desired shape.
The ndarray creation functions can create arrays with any dimension by specifying how many dimensions
and length along that dimension
in a tuple or list.
"""
import numpy as np
from numpy.random import default_rng

"""
numpy.zeros will create an array filled with 0 values with the specified shape. 
The default dtype is float64.
"""
anD_1 = np.zeros([3, 4])  # 用 list 或 tuple 指定都可以
print(f"anD_1:\n{anD_1}\n")
anD_2 = np.zeros((3, 4))
print(f"anD_2:\n{anD_2}\n")
anD_3 = np.zeros([2, 3, 4])
print(f"anD_3:\n{anD_3}\n")


"""
numpy.ones will create an array filled with 1 values. 
It is identical to zeros in all other respects
"""
anD_4 = np.ones((2, 3, 4))
print(f"anD_4:\n{anD_4}\n")


"""
The random method of the result of default_rng will create an array filled with random values between 0 and 1. 
It is included with the numpy.random library. 
The seed is set to 42
"""
anD_5 = default_rng(42).random([2, 3])
print(f"anD_5:\n{anD_5}\n")
anD_6 = default_rng(42).random([2, 3, 4])
print(f"anD_6:\n{anD_6}\n")


"""
numpy.indices will create a set of arrays (stacked as a one-higher dimensioned array), 
one per dimension with each representing variation in that dimension.
"""
anD_7 = np.indices((3, 4))
print(f"anD_7:\n{anD_7}\n")
