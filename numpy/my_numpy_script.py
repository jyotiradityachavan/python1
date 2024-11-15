# #1 dimensional array

# import numpy as np;
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[2])




# #2 dimensional array
# import numpy as np;
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print (arr[0,1])
# print(arr[1,3])
# print(arr[1,4])




# #3 dimensional array
# import numpy as np;
# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
# print(arr[0,1,2])
# print(arr[1,1,2])
# print (type(arr))
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)




#Arithemetic operation
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 * 2)




#matrix operation
import numpy as np;
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))
print(a.T)

