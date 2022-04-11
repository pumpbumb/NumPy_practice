import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [10, 11, 12, 13]])
b = a  # no new object is created

# a is b ,这是一个同一性运算符。用于比较两个对象的物理id。如果相同则返回True,否则返回False
print(a is b)  # a and b are two names for the same ndarray object
