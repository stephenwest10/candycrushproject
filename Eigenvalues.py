import numpy.matlib 
import numpy as np 
import matplotlib.pyplot as plt

matrix4 = np.array([[0, 1, 0, 0], [1/4, 0, 3/4, 0], [0, 2/4, 0, 2/4], [0, 0, 3/4, 0]])
matrix5 = np.array([[0, 1, 0, 0, 0], [1/5, 0, 4/5, 0, 0], [0, 2/5, 0, 3/5, 0], [0, 0, 3/5, 0, 2/5], [0, 0, 0, 4/5, 0]])
matrix6 = np.array([[0, 1, 0, 0, 0, 0], [1/6, 0, 5/6, 0, 0, 0], [0, 2/6, 0, 4/6, 0, 0], [0, 0, 3/6, 0, 3/6, 0], [0, 0, 0, 4/6, 0, 2/6], [0, 0, 0, 0, 5/6, 0]])
matrix7 = np.array([[0, 1, 0, 0, 0, 0, 0], [1/7, 0, 6/7, 0, 0, 0, 0], [0, 2/7, 0, 5/7, 0, 0, 0], [0, 0, 3/7, 0, 4/7, 0, 0], [0, 0, 0, 4/7, 0, 3/7, 0], [0, 0, 0, 0, 5/7, 0, 2/7], [0, 0, 0, 0, 0, 6/7, 0]])


print("Eigenvalues for 4x4: ", np.linalg.eigvals(matrix4))
print("Eigenvalues for 5x5: ", np.linalg.eigvals(matrix5))
print("Eigenvalues for 6x6: ", np.linalg.eigvals(matrix6))
print("Eigenvalues for 7x7: ", np.linalg.eigvals(matrix7))
