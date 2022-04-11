import numpy as np

a1 = np.arange(10)
print(f"a1[2]:\n{a1[-1]}\n")

a1.shape = (2, 5)  # now a1 is 2-dimensional. shape 是 ndarray 的一个 attribute .
print(f"a1:\n{a1}\n")

"""
Note that x[1, 3] == x[1][3] though the second case is more inefficient 
as(因为) a new temporary array is created after the first index that is subsequently indexed by 3.
(因为在第一个索引之后创建了一个新的临时数组(只是一个 view , 不是一个 copy )，该数组再被3索引)
"""
print(f"a1[1, 3]:\n{a1[1, 3]}\n")
print(f"a1[1][3]:\n{a1[1][3]}\n")

print(f"a1[0, -1]:\n{a1[0, -1]}\n")

print(f"a1[1]:\n{a1[1]}\ntype(a1[1]): {type(a1[1])}\na1[1].shape: {a1[1].shape}\n")
# a1[1]是一个 view ， 不是一个 copy , 看下面：
a1[1] = ([11, 12, 13, 14, 15])
print(f"a1:\n{a1}\n")

"""
1. Negative i and j are interpreted as n + i and n + j 
where n is the number of elements in the corresponding dimension. 
2. Negative k makes stepping go towards smaller indices. 
"""
a2 = np.array([12, 31, 67, 9, 256, 1412, 932, 48, 624, 241])
print(f"a2[2:9]:\n{a2[2:9]}\n")
print(f"a2[-6:9]:\n{a2[-6:9]}\n")  # -6 + 10 = 4 ， 故从index=4开始到index=9.
print(f"a2[-2:2:-3]:\n{a2[-2:2:-3]}\n")  # -3 表示倒着3个3个的来

# Note that :: is the same as : and means select all indices along this axis.
print(f"a2[-3:]:\n{a2[-3:]}\n")  # 从 -2 + 10 = 8 ， 即 index=8 开始

"""
If the number of objects in the selection tuple is less than N(维度的数量),
then : is assumed for any subsequent dimensions. 
"""
a3 = np.array([[[21], [52], [63]], [[104], [759], [666]], [[11], [33], [86]]])
print(f"a3.shape:\n{a3.shape}\n")
print(f"a3[1:2]:\n{a3[1:2]}\n")

####################################################################################################
# 注意理解以下内容：
arr = np.array(
    [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
     np.linspace(20, 47, 10).reshape(2, 5),
     np.linspace(50, 77, 10).reshape(2, 5),
     np.linspace(80, 107, 10).reshape(2, 5)])
print('\n', 'arr', arr, sep='\n')

# 对于一个有着3个axis的ndarray来说，索引的时候，第一部分代表对axis=0的索引，第二部分代表对axis=1
# 索引，第三部分代表对axis=2的索引
print('\n', 'arr[1:2, 1, 3]\n', arr[1::2, 1, 3])  # 这里第一部分省略了中间的stop，这表示一直选到最后一个
# 每一个axis都遵循 start stop step ， 不给start就表示从头开始选，不给stop就表示一直选到包括最后一个，不给step就是默认为 1 ，
# 若某一个axis没写，就表示此axis全选
