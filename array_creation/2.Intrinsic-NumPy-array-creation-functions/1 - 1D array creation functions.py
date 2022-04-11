# The 1D array creation functions e.g. numpy.arange and numpy.linspace
import numpy as np

"""
Note: best practice for numpy.arange is to use integer start, end, and step values.
arange：拆解为  a range  不要混淆了!
"""
a1D_1 = np.arange(2, 10, 3)  # 主要参数： start   stop   step  dtype
print(a1D_1, '\n')

"""
1. numpy.linspace will create arrays with a specified number of elements, 
and spaced equally between the specified beginning and end values. 
2. linspace: 拆解为 lin(linear)  space
3. The advantage of this creation function is that you guarantee 
the number of elements and the starting and end point. 
The previous arange(start, stop, step) will not include the value `stop`.
"""
a1D_2 = np.linspace(3, 8, 5, dtype=int)
print(a1D_2)
