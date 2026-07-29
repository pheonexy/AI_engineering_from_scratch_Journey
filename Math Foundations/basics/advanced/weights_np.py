import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A + B =\n", A + B)
print("A * B (element-wise) =\n", A * B)
print("A @ B (matrix multiply) =\n", A @ B)
print("A^T =\n", A.T)
print("det(A) =", np.linalg.det(A))
print("A^-1 =\n", np.linalg.inv(A))
print("I =\n", np.eye(2))

inputs = np.random.randn(3, 1)
weights = np.random.randn(2, 3)
bias = np.array([[0.1], [0.1]])
output = np.maximum(0, weights @ inputs + bias)

print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
print(f"Output:\n{output}")

'''
A + B =
 [[ 6  8]
 [10 12]]
A * B (element-wise) =
 [[ 5 12]
 [21 32]]
A @ B (matrix multiply) =
 [[19 22]
 [43 50]]
A^T =
 [[1 3]
 [2 4]]
det(A) = -2.0000000000000004
A^-1 =
 [[-2.   1. ]
 [ 1.5 -0.5]]
I =
 [[1. 0.]
 [0. 1.]]

Neural network layer: (2, 3) @ (3, 1) = (2, 1)
Output:
[[0.        ]
 [0.79203977]]
 '''
