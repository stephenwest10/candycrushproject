import numpy.matlib 
import numpy as np 
import matplotlib.pyplot as plt


valuesToPlot = []
t1 = np.arange(1, 100, 1)

for i in t1: 
    initialDist = np.array([0, 0, 1, 0, 0])
    Tmatrix = np.array([[0, 1, 0, 0, 0], [1/5, 0, 4/5, 0, 0], [0, 2/5, 0, 3/5, 0], [0, 0, 3/5, 0, 2/5], [0, 0, 0, 4/5, 0]])
    Tmatrixpower = np.linalg.matrix_power(Tmatrix, (i-1))
    T_0 = np.array([0, 0, 0, 0, 1/5])
    
    product1 = np.matmul(initialDist, Tmatrixpower)
    product2 = np.matmul(product1, T_0)
    print(product2)
    valuesToPlot.append(product2.item(0))

print(valuesToPlot)
plt.plot(t1, valuesToPlot)
plt.show()

