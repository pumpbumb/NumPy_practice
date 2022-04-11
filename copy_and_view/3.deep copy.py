import numpy as np

a = np.array([[56, 70, 31, 82],
              [471, 614, 741, 58],
              [59, 78, 12, 133]])

# The copy method makes a complete copy of the array and its data.
d = a.copy()  # a new array object with new data is created
print(f"d is a ? {d is a} \n d.base is a ? {d.base is a}"
      f"\t# d doesn't share anything with a\n")
d[0, 0] = 99999
print('a', a, 'd', d, sep='\n', end='\n\n')

# Sometimes copy should be called after slicing if the original array is not required anymore.
# For example, suppose a is a huge intermediate result and the final result b only contains a small fraction of a,
# a deep copy should be made when constructing b with slicing:
a = np.arange(int(1e8))
b = a[0:100].copy()
del a  # # the memory of a can be released.
