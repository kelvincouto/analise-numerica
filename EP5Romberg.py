import numpy as np


def function(x):
   func = x**2
   return func;

def trapez(a,b,t,i):
  #a e b dao o intervalo
  #t e o ultimo valor calculado
  #i e a quantidade de intervalos
  #newT e o valor do trapezio calculado
    h  = (b-a)/2**i
    if i==0:
      #Se i for zero, calcula o primeiro trapezio
      newT=(h/2)*(function(a)+function(b))
    
    else:     #Calculo dos trapezios, usando valor calculado previamente e pontos novos
      newPoints = np.arange(a+h,b,2*h)
      newFunctionsValues=function(newPoints)
      newTrapzSum=np.sum(newFunctionsValues)
      newT = (t/2) + h*newTrapzSum
    
    return newT


def romberg(a,b,n,erro,ITMAX):

  matrixRomberg=np.zeros((n+1,n+1))
  iterations=0
  convergence=0

  for i in range(0,n+1):
    matrixRomberg[i][0]=trapez(a,b,matrixRomberg[i-1][0],i)
    for j in range (0,i):
      matrixRomberg[i][j+1] = 1.0/(4**(j+1)-1)*(4**(j+1)*matrixRomberg[i][j] - matrixRomberg[i-1][j])
    iterations=iterations+1
    if i>0:
      if abs(matrixRomberg[i][i]-matrixRomberg[i][i-1])<(erro*matrixRomberg[i][i]):
        convergence=1

        return matrixRomberg[i][i],iterations,convergence
      elif iterations>=ITMAX:
        convergence=2
        return matrixRomberg[i][i],iterations,convergence

  
  return matrixRomberg[-1][-1],iterations,convergence

#Valores Iniciais
intervalStart=0
intervalEnd=1
tol=1e-15
n=15
ITMAX=15

result,iterationNumber,didItConverge=romberg(intervalStart,intervalEnd,n,tol,ITMAX)
if didItConverge == 2:
  print("O metodo de Romberg nao convergiu apos ",iterationNumber, " iteracoes e o resultado mais proximo foi ", result)
elif didItConverge ==1 :
  print("O metodo de Romberg convergiu apos ",iterationNumber, " iteracoes e o resultado foi ", result)
else:
  print("O metodo de Romberg nao convergiu pois a quantidade de colunas delimitada foi insuficente, e o resultado mais proximo foi ", result)

