import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('exam_A_dataset.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

def polyfit(x, y, n):
    xlen = len(x)
    ylen = len(y)
    one = np.ones((xlen,n+1), dtype=int)
    print (one)
    xT = np.matrix(x)
    yT = np.matrix(y)
    c2 = np.power(xT,2)  #generar el cuadrado
    print(xT)
    c1 = one[:,[1]]    #selecciona la columna 1
    print(c1)
    A = np.hstack([c1,xT.getT(),c2.getT()])   #aplica la matriz transpuesta
    print(A)

    def inv(A):
        return np.linalg.inv(A)
    def transp(A):
        return A.getT()
    def prod(A,B):
        return np.dot(A,B)

    AtA = inv(prod(transp(A),A))
    print(AtA)
    up = prod(AtA,transp(A))
    u = prod(up,transp(yT))

    print(u)


x=[1,-2,3,4]
y=[1,4,9,16]
plt.scatter(x,y)
plt.show()
polyfit(x,y,1)
