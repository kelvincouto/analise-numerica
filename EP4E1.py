import numpy as np
from matplotlib import pyplot as plt

def Thomas (a,b,d):
  z=len(a)
  for i in range (1,z):
    #Calcula a diagonal principal e o novo d
      a[i]=a[i]-(b[i-1]*b[i-1]/a[i-1])
      d[i]=d[i]-(b[i-1]*d[i-1]/a[i-1])
  
  #Calculo do vetor x
  x=np.zeros(z)
  x[-1]=d[-1]/a[-1]

  for i in range (z-2,-1,-1):
    x[i]=(d[i]-(b[i]*x[i+1]))/a[i]
  
  return x

def calculoFuncao (n):
  h=1/(n+1)
  l=0 # valor de lambda
  a=np.zeros(n)
  b=np.zeros(n-1)
  d=np.zeros(n)

  for i in range(0,n):
    a[i]=(2/h)

  for i in range(0,n-1):
    b[i]=(-1/h)

  for i in range(0,n):
    d[i]=h

  
  # Cria a matrix tridiagonal dada
  aDiagonal=np.diagflat(a)
  bDiagonal=np.diagflat(b,1)
  cDiagonal=np.diagflat(b,-1)
  matrix=aDiagonal+bDiagonal+cDiagonal
  

  x=Thomas(a,b,d)

  erro=np.zeros(n)
  for i in range (0,n):
    xi=(i+1)*h
    u=0.5*xi*(1-xi)
    erro[i]=abs((u-x[i]))
  
  
  return(erro.max())

valoresDeN=np.array([15,31,63,127,255])
valoresDeErro=np.zeros(len(valoresDeN))

for i in range (0,len(valoresDeN)):
  valoresDeErro[i]=calculoFuncao(valoresDeN[i])
  print(" Para o valor de n: ",valoresDeN[i], "temos o erro: ", valoresDeErro[i])


plt.plot(valoresDeN,valoresDeErro)
plt.xlabel("Valores de N")
plt.ylabel("Erro")
plt.title("Erro por N")
plt.show()