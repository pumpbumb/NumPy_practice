# NumPy arrays can be defined using Python sequences such as lists and tuples.
import numpy as np

a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.float32)  # 创建 ndarray, 并确定数据类型
print(a3D)
print(a3D.ndim)  # the number of axes (dimensions) of the array.
print(a3D.shape)  # 由外向内去数 axes(dimensions) ，技巧：嵌套几个中括号就是几维~
print(a3D.size)  # the total number of elements of the array. This is equal to the product of the elements of shape.

# the size in bytes of each element of the array. For example, an array of elements of type
# float64 has itemsize 8 (=64/8)
print(a3D.itemsize)
