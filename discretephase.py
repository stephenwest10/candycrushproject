import numpy.matlib 
import numpy as np 
import matplotlib.pyplot as plt


valuesToPlot = []
t1 = np.arange(1, 100, 1)
#t1 defines a range of values to plot over
initialDist = np.array([1, 0, 0, 0, 0])
#Change this initial distribution depending on where you start
Tmatrix = np.array([[0, 4/5, 0, 0, 0], [2/5, 0, 3/5, 0, 0], [0, 3/5, 0, 2/5, 0], [0, 0, 4/5, 0, 1/5], [0, 0, 0, 1, 0]])
print("Eigenvalues: ", np.linalg.eigvals(Tmatrix))
#to show the eigenvalues of this matrix

for i in t1: 
   
    Tmatrixpower = np.linalg.matrix_power(Tmatrix, (i-1))
    T_0 = np.array([1/5, 0, 0, 0, 0])
    product1 = np.matmul(initialDist, Tmatrixpower)
    product2 = np.matmul(product1, T_0)
    valuesToPlot.append(product2.item(0))

#print(valuesToPlot) #output data if want to collect
plt.bar(t1, valuesToPlot)
plt.xlabel("Number of Moves/Timesteps")
plt.ylabel("Probability")
plt.title("PMF of a Discrete-Phase Distribution given we start in State 1")
#Edit this title depending on start point
plt.show()

