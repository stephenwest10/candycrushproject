import numpy.matlib 
import numpy as np 
import matplotlib.pyplot as plt


valuesToPlot = []
t1 = np.arange(1, 100, 1)
initialDist = np.array([0, 0, 0, 0, 1])
Tmatrix = np.array([[0, 1, 0, 0, 0], [1/5, 0, 4/5, 0, 0], [0, 2/5, 0, 3/5, 0], [0, 0, 3/5, 0, 2/5], [0, 0, 0, 4/5, 0]])
print("Eigenvalues: ", np.linalg.eigvals(Tmatrix))

for i in t1: 
   
    Tmatrixpower = np.linalg.matrix_power(Tmatrix, (i-1))
    T_0 = np.array([0, 0, 0, 0, 1/5])
    
    
    product1 = np.matmul(initialDist, Tmatrixpower)
    product2 = np.matmul(product1, T_0)
    #print(product2)
    valuesToPlot.append(product2.item(0))

#print(valuesToPlot)
plt.bar(t1, valuesToPlot)
plt.xlabel("Number of Moves/Timesteps")
plt.ylabel("Probability")
plt.title("PDF of a Discrete Phase Distribution given we start in State 4")
plt.show()

