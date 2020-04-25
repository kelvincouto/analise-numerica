import numpy as np

def decomposicaoLDLT (a,b):
  n=len(a)
  L=np.zeros(n-1)
  D=np.zeros(n)
  
  D[0]=a[0]

  for i in range(0,n-1):
      L[i]=b[i]/D[i]
      x=L[i]*L[i]*D[i]
      D[i+1]=a[i+1]-x

  return (L,D)

def resolucaoMatriz (L,D,d):
  n=len(D)
  x=np.zeros(n)
  y=np.zeros(n)
  z=np.zeros(n)
  
  z[0]=d[0]
  y[0]=z[0]/D[0]

  for i in range(1,n):
    #Calculo de Lz=d
      z[i]=d[i]-(L[i-1]*z[i-1])
    #Calculo de Dy=z
      y[i]=z[i]/D[i]


  x[-1]=y[-1]

  for i in range(n-2,-1,-1):
    #Calculo de L't*x=y
    x[i]=y[i]-(L[i]*x[i+1])
  

  return x


#Inputs
a=np.array([4.0,4,4,4,4])
b=np.array([1,1,1,1])
#resultado de Ax=d
d=np.array([3.0,3,3,3,3])
# Cria a matrix tridiagonal dada para testes
aDiagonal=np.diagflat(a)
bDiagonal=np.diagflat(b,1)
cDiagonal=np.diagflat(b,-1)
matrix=aDiagonal+bDiagonal+cDiagonal

L,D=decomposicaoLDLT(a,b)

x=resolucaoMatriz(L,D,d)

print("Seu vetor L e: \n")
print(L)

print("\n Seu vetor D e: \n")
print(D)

print("\n Seu resultado x e: \n")
print(x)