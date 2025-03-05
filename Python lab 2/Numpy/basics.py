import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)

# Shape and Reshape
arr2_shape = arr2.shape
reshaped = arr2.reshape(3, 2)
flattened = arr2.flatten()

# Basic Operations
sum_arr = arr1 + arr1
sub_arr = arr1 - arr1
mul_arr = arr1 * 2
div_arr = arr1 / 2
exp_arr = np.exp(arr1)
sqrt_arr = np.sqrt(arr1)
dot_product = np.dot(arr1, arr1)

# Aggregate Functions
mean_val = np.mean(arr2)
median_val = np.median(arr2)
std_dev = np.std(arr2)
var_val = np.var(arr2)
min_val = np.min(arr2)
max_val = np.max(arr2)

# Slicing and Indexing
slice1 = arr2[0, :]
slice2 = arr2[:, 1]
boolean_mask = arr2[arr2 > 2]

# Stacking and Concatenation
vstacked = np.vstack((arr1, arr1))
hstacked = np.hstack((arr1, arr1))
concatenated = np.concatenate((arr1, arr1), axis=0)

# Broadcasting 
"""
Broadcasting is a feature that allows NumPy to perform operations on arrays of different shapes without explicit looping.
It automatically expands smaller arrays to match the shape of larger ones.
"""
broadcasted = arr1 + np.array([[1], [2], [3]]) # arr1 is added to every element pf 2D array
print(broadcasted)

# Axis Operations
axis_sum_0 = np.sum(arr2, axis=0)  # Sum along columns
axis_sum_1 = np.sum(arr2, axis=1)  # Sum along rows
axis_mean_0 = np.mean(arr2, axis=0)  # Mean along columns
axis_mean_1 = np.mean(arr2, axis=1)  # Mean along rows

# Linear Algebra
inverse = np.linalg.inv(np.array([[1, 2], [3, 4]]))
det = np.linalg.det(np.array([[1, 2], [3, 4]]))
eigenvalues, eigenvectors = np.linalg.eig(np.array([[1, 2], [3, 4]]))

# Saving and Loading
np.save("array.npy", arr1)
loaded_array = np.load("array.npy")

print("All operations executed successfully!")
