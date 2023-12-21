# Numpy provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level
# mathematical functions to operate on these arrays

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# Array attributes
print(arr_1d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# output : 1
print(arr_1d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# Output : (5,)
print(arr_1d.size)  # size: Provides the total number of elements in the array.
# Output : 5


print("----------Array Simple Operations------------------")
arr = np.array([1, 2, 3, 4, 5])
print(np.sqrt(arr))  # square root
print(np.sum(arr))  # sum
print(np.mean(arr))  # average
print(np.max(arr))  # max
print(np.min(arr))  # min

print("----------2D array------------")

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print(arr_2d.ndim)  # 2
print(arr_2d.shape)  # (2, 3)
print(arr_2d.size)  # 6

print("transpose: ", arr_2d.T)
print("reshaped: ", arr_2d.reshape(3, 2))

print("-----------Access elements of array-----------")
print(arr_1d[3])  # access 3 element
print(arr_2d[0])  # get the first row

print(arr_2d[0, 1])  # get the first row, second column

print(arr_2d[:, 1])  # get the second column
print(arr_2d[1, :])  # get the second row

print("-------------------------------")
print("--------Array Addition-------------")
array1 = np.array([2, 3, 4])
array2 = np.array([3, 4, 5])
sumOfArray = array1 + array2
print(sumOfArray)

# Scalar multiplication
print("--------Scalar multiplication-------------")
array = np.array([1, 2, 3])
result = array * 2  # each element of an array is multiplied by 2
print(result)  # [2 4 6]

print("----------Hadamard Product (element wise multiplication)---------------")
# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
print(array1)
array2 = np.array([4, 5, 6])
print(array2)
result = array1 * array2
print(result)  # [4 10 18]

print("-------------Matrix multiplication------------------")
matrix1 = np.array([[1, 2], [3, 4]])
print("matrix1: ", matrix1)
matrix2 = np.array([[5, 6], [7, 8]])
print("matrix2: ", matrix2)
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]


a = np.array([-1, 1])
b = np.array([1, 1])
print(np.dot(a, b))

X = np.array([[1, 0, 1], [2, 2, 2]])
out = X[0, 1:3]
print(out)
