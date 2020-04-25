import numpy as np


def decomposicaoCholesky(matrix):
  n=len(matrix)
  cholesky=np.zeros(shape=(n,n))
  cholesky[0][0]=np.sqrt(matrix[0][0])
  for i in range (1,n):
    cholesky[i][0] = matrix [i][0]/cholesky[0][0]
  
  for j in range (1,n):
    for i in range (0,n):
      if j>i:
        #Triangulo superior é nulo
        cholesky[i][j]=0
      elif i==j:
      #Cálculo das diagonais
        somaLinha = 0
        for k in range (0,i):
          #Soma dos Quadrados
          somaLinha = somaLinha + (cholesky[i][k]*cholesky[i][k])
        cholesky[i][j]=np.sqrt(matrix[i][i]- somaLinha)
      else:
        #Calculo Aij
        somaLinha = 0
        for k in range (0,j):
          #Soma da Linha Anterior
          somaLinha = somaLinha + cholesky[i][k]*cholesky[j][k]
        cholesky[i][j]=(matrix[i][j]-somaLinha)/cholesky[j][j]
      
  return(cholesky)


def decomposicaoLDL(cholesky):
  n=len(cholesky)
  D1=np.diag(B)
  L=np.zeros(shape=(n,n))
  for j in range (0,n):
    for i in range (0,n):
      if j>i:
        #Triangulo superior nulo
        L[i][j]=0
      elif j == i:
        L[i][j]=1
      else:
        L[i][j]=cholesky[i][j]/D1[j]
  D=D1*D1

  return (L,D)



a=np.array([4.0,4,4,4,4])
b=np.array([1.0,1,1,1])

# Cria a matrix tridiagonal dada
aDiagonal=np.diagflat(a)
bDiagonal=np.diagflat(b,1)
cDiagonal=np.diagflat(b,-1)
matrix=aDiagonal+bDiagonal+cDiagonal

B=decomposicaoCholesky(matrix)
L,D= decomposicaoLDL(B)
print("A matriz L sera: \n")
print(L)
print( "\n A matriz D sera: \n")
print(D)


