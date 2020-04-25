import numpy as np

def Thomas (a,b,d):
  n=len(a)
  for i in range (1,n):
    #Calcula a diagonal principal e o novo d
      a[i]=a[i]-(b[i-1]*b[i-1]/a[i-1])
      d[i]=d[i]-(b[i-1]*d[i-1]/a[i-1])
  
  #Calculo do vetor x
  x=np.zeros(n)
  x[-1]=d[-1]/a[-1]

  for i in range (n-2,-1,-1):
    x[i]=(d[i]-(b[i]*x[i+1]))/a[i]
  
  return x





a=np.array([4.0,4,4,4,4])
b=np.array([1,1,1,1])
d=np.array([3.0,3,3,3,3])
# Cria a matrix tridiagonal dada
aDiagonal=np.diagflat(a)
bDiagonal=np.diagflat(b,1)
cDiagonal=np.diagflat(b,-1)
matrix=aDiagonal+bDiagonal+cDiagonal

x=Thomas(a,b,d)


D=matrix.dot(x)
print("Seu resultado e: \n")
print(x)